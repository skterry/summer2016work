import numpy as np
import pyfits
from astropy.coordinates import ICRS
from astropy import units as u
import glob
import csv

def match_objects(folder_labels):

        print("----------------------------------------")
        print("Running Module 2: Match Objects")

        # stores all "_" filter txt files (eventually will group by similar exposure times in event there are more than one J,Ks files
        j_files = np.hstack(np.array(glob.glob('Data/{}/*-J.txt'.format(folder))) for folder in folder_labels)
        k_files = np.hstack(np.array(glob.glob('Data/{}/*-Ks.txt'.format(folder))) for folder in folder_labels)

        print j_files
        print k_files
        j_filter_data = np.empty([0,5])
        ra1 = np.empty([0,1])
        ra2 = np.empty([0,1])

        k_filter_data = np.empty([0,5])
        dec1 = np.empty([0,1])
        dec2 = np.empty([0,1])

        print '\nPlease wait while all data is loaded from files...'
        
        # appends data from all J filter files in folder if multiple 
        for j in j_files:
                # generate numpy array from txt files
                new_data1 = np.genfromtxt(j, unpack = False)
                j_filter_data = np.vstack([j_filter_data, new_data1])
                print 'Data from J filter file', j, 'loaded...'
                print j_filter_data.shape
                
        ra1 = j_filter_data[:,3]
        dec1 = j_filter_data[:,4]
        print 'J Filter shape:', ra1.shape, dec1.shape

        # appends data from all Ks filter files in folder if multiple
        for k in k_files:
                new_data2 = np.genfromtxt(k, unpack = False)              
                k_filter_data = np.vstack([k_filter_data, new_data2])
                print 'Data from Ks filter file', k, 'loaded...'
                print k_filter_data.shape

        ra2 = k_filter_data[:,3]
        dec2 = k_filter_data[:,4]
        print 'Ks Filter shape:', ra2.shape, dec2.shape

        print 'Data from all files loaded.'
        print '\nPlease wait while objects are matched across the J and Ks Filter...'
        # j filter ra/dec info to be compared
        # in units of degrees
        obj_1 = ICRS(ra1, dec1, unit=(u.degree, u.degree))

        # k filter ra/dec info to be compared
        # in units of degrees
        obj_2 = ICRS(ra2, dec2, unit=(u.degree, u.degree))

        # This function will match all objects from obj_1 (j-filter) with an object in obj_2 (ks-filter)
        # By its nature, match_to_catalog_sky compares object data against catalog of sky, which would yield a closest match for every object
        # In our application, we compare two different sets of object data to each other, which should not guarantee a match
        # This means that we will get as many matches as there are objects in the smaller object data set (in this case, the j-filter will always have less objects)
        # This could be problematic since a "closest" match will be made relative to the available objects in obj_2 (ks-filter)
        # So a match does not necessarily constitute a match for us
        # To remedy this, I have run the matched objects through another test to compare the sum of differences against a set tolerance
        # This will ensure that all matches are within a controlled and tolerable closeness
        idx, d2d, d3d = obj_1.match_to_catalog_sky(obj_2) # match j band to k band since there are more objects in k

        # gets data matches from k-filter data based on matched indexes returned by match_to_catalog_sky
        matches = k_filter_data[idx,:]

        # appends all data columns for matched objects in a [:,10] array
        # j-filter
        #   0 -> Classification
        #   1 -> Aper_flux_3
        #   2 -> Aper_flux_3_err
        #   3 -> RA
        #   4 -> DEC
        # k-filter
        #   5 -> Classification
        #   6 -> Aper_flux_3
        #   7 -> Aper_flux_3_err
        #   8 -> RA
        #   9 -> DEC
        filter_matches = np.column_stack([j_filter_data, matches])

        # CHANGE THE TOLERANCE TO SEE WHAT WORKS BEST
        tolerance = 0.0001

        # compares sum of differences between RA/DEC values to set tolerance to ensure quality matches
        # see long comment above to see reasoning
        within_tol_index = ((abs(filter_matches[:,3]-filter_matches[:,8]) < tolerance) & (abs(filter_matches[:,4]-filter_matches[:,9]) < tolerance)).nonzero()
        
        stellar_obj_matches = (np.squeeze((filter_matches[within_tol_index,:]), axis=0))

        print '\nNumber of matches found', stellar_obj_matches.shape
        np.savetxt('Resources/J_Ks-matches.txt', stellar_obj_matches, fmt=['%.1f', '%.10f', '%.10f', '%.10f', '%.10f','%.1f', '%.10f', '%.10f', '%.10f', '%.10f'], delimiter=' ')

if __name__ == "__main__":
	
	# this part of the code runs if this file is being run independently
	# this part of the code doesn't run if it's just being imported as a module into 0_all.py
	# so, having this check for whether name == main makes sure that this part isn't run in 0_all.py
	# which prevents running each method twice in all.py
	# but also allows this file to be run by itself with no modifications

	#folder_labels = np.array(['B306', 'B307', 'B320', 'B321', 'B337', 'B338', 'B339', 'B340', 'D063', 'D064', 'D065', 'D066'])
	#folder_labels = np.array(['B338'])
	folder_labels = np.array(['B306', 'B307', 'B320', 'B321', 'B338', 'B339', 'B340'])
	#folder_labels = np.array(['D063', 'D064', 'D065', 'D066'])
	match_objects(folder_labels)
