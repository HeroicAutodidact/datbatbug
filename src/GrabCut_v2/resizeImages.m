fnames = dir('../../../repository/datbatbug/images/samples/*JPG');
numfids = length(fnames);
for K = 1:numfids
  img = imread(sprintf('../../../repository/datbatbug/images/samples/%s', fnames(K).name));
  img = imresize(img, .1);
  imwrite(img, sprintf('images/%i.jpg', K));
end