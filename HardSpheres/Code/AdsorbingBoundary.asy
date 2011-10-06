size(6cm);

// Pen for drawing labels
import fontsize;

pen label_pen=fontsize(10);
defaultpen(label_pen);

// Axes
import graph;

// h
real [] hticks = {1,2,3,4,5};
string hLabels(real z) {
    return string(z-1);
    }
xequals(L="$h/a$", 0.0, ymin=0.0, ymax=6.0, ticks=LeftTicks(format=Label(align=left),
            ticklabel=hLabels, hticks), Arrow);

// Surfaces
import patterns;
add("hatch",hatch(2mm));

path surface = (0,0)--(4,0)--(4,-1)--(0,-1)--cycle;
pen fpen = gray(0.5);
fill(surface, p=fpen);
draw((0,0)--(4,0));

// Particles
path particle1 = circle((2,1), 1.0);
path particle2 = circle((2,3), 1.0);

draw(particle1);
draw(particle2);

// Interaction zone
draw((0,1)--(4,1), p=dashed);
draw((0,3)--(4,3), p=dashed);
