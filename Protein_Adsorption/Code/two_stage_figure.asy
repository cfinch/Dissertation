size(2.2 inches);
unit(1 inch);
defaultpen(black + fontsize(14pt));

real radius = 0.2;
pen protein_pen = rgb(0, 0, 1)+linewidth(0.3);
pen arrow_pen = black + linewidth(2.0);
pen surface_pen = gray(0.5);

// Two-stage model
fill(circle((0.4, 1.1), radius), p=protein_pen);
draw((0.4, 0.8)--(0.4, 0.5), arrow_pen, EndArrow(size=10.0));

fill(circle((0.4, radius), radius), p=protein_pen);
draw((0.7, radius)--(1.1, radius), arrow_pen, EndArrow(size=10.0));
label("$\alpha$", (0.0, radius));
label("$\sigma_{\alpha}$", (0.5, -0.2));

fill(ellipse((1.6, radius/2), 2*radius, radius/2), p=protein_pen);
label("$\beta$", (1.8, 0.4));
label("$\sigma_{\beta}$", (1.8, -0.2));

// Surface
fill(box((0.25, -0.1), (2.1, 0.0)), surface_pen);
