import numpy as np
from skimage import img_as_float, io
import os

def K_Means_Clustering_Algorithm(imgVectors, number_of_iterations, k):
    
    clusters = np.random.rand(k, 3)
    arr_vectors = np.full(imgVectors.shape[0], -1)
    
    for i in range(number_of_iterations):
        print('Running Iteration number ' + str(i + 1))
        label_pts = [None for ith_k in range(k)]
        
        for ith_rgb, rgb_val in enumerate(imgVectors):
            row = np.repeat(rgb_val, k).reshape(3, k).T
            var = np.linalg.norm(row - clusters, axis=1)
            closestPoint = np.argmin(var)
            arr_vectors[ith_rgb] = closestPoint

            if (label_pts[closestPoint] is None):
                label_pts[closestPoint] = []

            label_pts[closestPoint].append(rgb_val)

        for ith_k in range(k):
            if (label_pts[ith_k] is not None):
                point = label_pts[ith_k]
                sum_of_points = np.asarray(point).sum(axis=0)
                total_num_of_points = len(point)
                newClusters = sum_of_points / total_num_of_points
                clusters[ith_k] = newClusters

    return arr_vectors, clusters


if __name__ == '__main__':
    
    k_range = np.array([5, 10])
    image1_filename = 'Koala.jpg'
    image2_filename = 'Penguins.jpg'
    
    print('For first image(Koala.jpg):')
    print('')
    for k in k_range:
        print('When k =',k,':')
        image = io.imread(image1_filename)[:, :, :3] 
        image = img_as_float(image)
        dimensions_of_img = image.shape
        image_name = image
        imgVectors = image.reshape(-1, image.shape[-1])
        numOfIterations = 100
    
        arr, cluster_mean = K_Means_Clustering_Algorithm(imgVectors, numOfIterations, k)
        output_image = np.zeros(imgVectors.shape)
        
        for i in range(output_image.shape[0]):
            output_image[i] = cluster_mean[arr[i]]
    
        output_image = output_image.reshape(dimensions_of_img)
        
        io.imsave('KoalaAfterCompressionfor_k='+str(k)+'.jpg' , output_image)
        
        img_info = os.stat(image1_filename)
        print("Original image size: ",img_info.st_size/1024,"KB")
        
        compressed_img_info = os.stat('KoalaAfterCompressionfor_k='+str(k)+'.jpg')
        print("Image size after Compression : ",compressed_img_info.st_size/1024,"KB")
        print('')
        
    print('')
    print('For second image(Penguins.jpg):')
    print('')
    for k in k_range:
        print('When k =',k,':')
        image = io.imread(image2_filename)[:, :, :3] 
        image = img_as_float(image)
        dimensions_of_img = image.shape
        image_name = image
        imgVectors = image.reshape(-1, image.shape[-1])
        numOfIterations = 100
    
        arr, cluster_mean = K_Means_Clustering_Algorithm(imgVectors, number_of_iterations = numOfIterations, k = k)
        output_image = np.zeros(imgVectors.shape)
        
        for i in range(output_image.shape[0]):
            output_image[i] = cluster_mean[arr[i]]
    
        output_image = output_image.reshape(dimensions_of_img)

        io.imsave('PenguinsAfterCompressionfor_k='+str(k)+'.jpg' , output_image)
        
        img_info = os.stat(image2_filename)
        print("Original image size: ",img_info.st_size/1024,"KB")
        
        compressed_img_info = os.stat('PenguinsAfterCompressionfor_k='+str(k)+'.jpg')
        print("Image size after Compression : ",compressed_img_info.st_size/1024,"KB")
        print('')