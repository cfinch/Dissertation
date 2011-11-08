import three;

viewportmargin = (0.2cm, 0.2cm);
size(3inches);
defaultpen(linewidth(1.0));

real domain_size = 100;
real radius = 5.0;

currentprojection = orthographic(domain_size*1.5, domain_size*2, domain_size, zoom=1, center=true);

// Simlation domain
path3[] domain = scale3(domain_size)*box(O,(1,1,1));
draw(domain);
path3 surf =((0,0,0)--(0,domain_size,0)--(domain_size,domain_size,0)--(domain_size,0,0)--cycle);
draw(surface(surf), gray, nolight);

// Particles in solution
triple c1 = (10,10,43);
triple c2 = (50,23,89);
triple c3 = (92,87,74);
triple c4 = (17,56,59);
triple c5 = (33,42,39);
triple c6 = (61,59,92);
triple c7 = (9,82,34);
triple c8 = (85,18,34);

surface p1=shift(c1)*scale3(radius)*unitsphere;
surface p2=shift(c2)*scale3(radius)*unitsphere;
surface p3=shift(c3)*scale3(radius)*unitsphere;
surface p4=shift(c4)*scale3(radius)*unitsphere;
surface p5=shift(c5)*scale3(radius)*unitsphere;
surface p6=shift(c6)*scale3(radius)*unitsphere;
surface p7=shift(c7)*scale3(radius)*unitsphere;
surface p8=shift(c8)*scale3(radius)*unitsphere;
draw(p1, blue);
draw(p2, blue);
draw(p3, blue);
draw(p4, blue);
draw(p5, blue);
draw(p6, blue);
draw(p7, blue);
draw(p8, blue);

// Brownian motion vectors
path3 arrow1 = (c1 -- (c1.x + 9, c1.y - 3, c1.z + 7));
path3 arrow2 = (c2 -- (c2.x - 2, c2.y + 8, c2.z + 5));
path3 arrow3 = (c3 -- (c3.x + 5, c3.y - 3, c3.z + 8));
path3 arrow4 = (c4 -- (c4.x - 5, c4.y + 10, c4.z - 6));
path3 arrow5 = (c5 -- (c5.x + 8, c5.y - 3, c5.z + 6));
path3 arrow6 = (c6 -- (c6.x - 7, c6.y - 3, c6.z - 12));
path3 arrow7 = (c7 -- (c7.x - 9, c7.y + 6, c7.z + 11));
path3 arrow8 = (c8 -- (c8.x - 5, c8.y + 3, c8.z - 8));
draw(arrow1, red, Arrow3);
draw(arrow2, red, Arrow3);
draw(arrow3, red, Arrow3);
draw(arrow4, red, Arrow3);
draw(arrow5, red, Arrow3);
draw(arrow6, red, Arrow3);
draw(arrow7, red, Arrow3);
draw(arrow8, red, Arrow3);

// Adsorbed particles
surface a1=shift((11,61,radius))*scale3(radius)*unitsphere;
surface a2=shift((90,67,radius))*scale3(radius)*unitsphere;
surface a3=shift((56,13,radius))*scale3(radius)*unitsphere;
surface a4=shift((42,34,radius))*scale3(radius)*unitsphere;
surface a5=shift((11,17,radius))*scale3(radius)*unitsphere;
surface a6=shift((76,41,radius))*scale3(radius)*unitsphere;
surface a7=shift((61,73,radius))*scale3(radius)*unitsphere;
surface a8=shift((46,93,radius))*scale3(radius)*unitsphere;

draw(a1);
draw(a2);
draw(a3);
draw(a4);
draw(a5);
draw(a6);
draw(a7);
draw(a8);
