function [perc_path, area_path] = pathCalc(img, mask)
    %pathCalc Function to calculate the relative percentage of pathogen on the
    %bat and find pathogen area in cm^2.
    %   Function returns "-1" for variable area_path if it cannot find the 
    %   penny to scale the image.

    % finds relative percentage of pathogen
    mask = logical(mask);
    [BW, ~] = createMask2(img); % make pathogen mask
    BW = BW.*mask;
    % calculate percentage of pathogen on bat in image
    perc_path = bwarea(BW)/bwarea(mask);

    low_rng = 0.05*size(img,1); high_rng = 0.1154*size(img,1);
    % find circles in image
    [~, radii] = imfindcircles(img,round([low_rng high_rng]),'ObjectPolarity','dark');
    % if we cant recognize circle, print error and return
    if isempty(radii)
        disp('Could not find penny, moving to next image');
        area_path = -1;
        return;
    end

    % calculate area in cm^2
    pa_pix = pi*radii(1)^2;
    pa_cm = 2.85; % penny area in cm^2
    area_path = bwarea(BW)*pa_cm/pa_pix;
end

