function [ absolutePathogen, relativePathogen ] = analyzeBatImage( file_path )
    addpath('GrabCut_v2');
    rawBatImg = imresize(imread(file_path), .2);
    
    warning('off', 'stats:kmeans:FailedToConverge')    
    equalizedBatImg = zeros(size(rawBatImg), 'uint8');
    equalizedBatImg(:,:,1) = adapthisteq(rawBatImg(:,:,1));
    equalizedBatImg(:,:,2) = adapthisteq(rawBatImg(:,:,2));
    equalizedBatImg(:,:,3) = adapthisteq(rawBatImg(:,:,3));
    mask = GC_GUI(equalizedBatImg);
    [absolutePathogen, relativePathogen] = pathCalc(rawBatImg, mask);
end


