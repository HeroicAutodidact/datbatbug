function [a] = triarea(b,h)
    a = 0.5*(b.* h);
    plot([1 3 4], [0 2 0], 'r--');
    hold on;
    ginput(1);
end