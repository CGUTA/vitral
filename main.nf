
raw_file = Channel.fromPath("${params.input}")
	.map { file -> tuple(file.baseName, file) }

process kmean_colors {
    conda "scipy scikit-learn opencv"

    publishDir "${params.out}", mode: 'copy', saveAs: { filename -> "${datasetID}_${params.colors_number}_colors_$filename" }
    
    input:
    set datasetID, file(input_image) from raw_file

    output:
    set datasetID, file("composition.png") into to_normalize


    """
    #!/usr/bin/env python3

    import cv2
    from sklearn.cluster import KMeans
    from scipy.cluster.vq import kmeans,vq

    image_raw = cv2.imread("$input_image", cv2.IMREAD_COLOR)

    image_hsv = cv2.cvtColor(image_raw, cv2.COLOR_BGR2HSV)

    def our_flatten(arr):
        return(arr.reshape(-1, arr.shape[-1]))
        
    image_kmeans = KMeans(n_clusters=$params.colors_num, random_state=0).fit(our_flatten(image_hsv))
        
    counter = 0
    for i in range(len(image_hsv)):
        for j in range(len(image_hsv[i])):
            #print(image_hsv[i][j])
            cluster_nummer = image_kmeans.labels_[ counter ]
            image_hsv[i][j] = image_kmeans.cluster_centers_[cluster_nummer]
            counter += 1

            
    image_bgr = cv2.cvtColor(image_hsv, cv2.COLOR_HSV2BGR)
            
    cv2.imwrite('composition.png', image_bgr)
    """

}
