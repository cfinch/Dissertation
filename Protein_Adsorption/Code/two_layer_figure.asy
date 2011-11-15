size(2.7 inches);
unit(1 inch);
defaultpen(black + fontsize(14pt));

real radius = 0.2;
pen protein_pen = rgb(0, 0, 1)+linewidth(0.3);
pen arrow_pen = black + linewidth(2.0);
pen surface_pen = gray(0.5);

// Multi-layer model
fill(circle((0.5, 1.2), radius), p=protein_pen);
draw((0.5, 0.9)--(0.5, 0.5), arrow_pen, EndArrow(size=10.0));
draw((0.7, 1.0)--(0.9, 0.8), arrow_pen, EndArrow(size=10.0));
label("A", (0.1, 1.2));
label("AB", (0.1, radius));
label("AAB", (1.1, 1.0));

pair[] centers = {(0.5, radius), (1.0, radius), (1.4, radius), (1.9, radius), 
    (2.5, radius),
    (1.0, 3*radius), (1.4, 3*radius), (1.9, 3*radius)}; 

for (pair center: centers) {
    fill(circle(center, radius), p=protein_pen);
}

// Surface
fill(box((0.25,-0.1), (2.7,0.0)), surface_pen);
