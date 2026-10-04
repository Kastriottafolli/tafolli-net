"""Generate the original static mesh fallback for the animated hero."""
import math
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent

def rotate(x,y,z):
    ax,ay,az=1.02,.32,-.56
    yy=y*math.cos(ax)-z*math.sin(ax)
    zz=y*math.sin(ax)+z*math.cos(ax)
    xx=x*math.cos(ay)+zz*math.sin(ay)
    zz=-x*math.sin(ay)+zz*math.cos(ay)
    return xx*math.cos(az)-yy*math.sin(az),xx*math.sin(az)+yy*math.cos(az),zz

def build():
    points,normals,faces=[],[],[]
    for i in range(65):
        u=i/64*math.pi*2
        row,normal=[],[]
        for j in range(25):
            v=j/24*math.pi*2
            minor=.56+.09*math.sin(5*u)+.035*math.sin(3*v)
            radius=1.23+minor*math.cos(v)
            x,y,z=rotate(radius*math.cos(u),radius*math.sin(u),minor*math.sin(v))
            perspective=5.4/(5.4-z)
            row.append((320+x*145*perspective,315+y*145*perspective,z))
            normal.append(rotate(math.cos(v)*math.cos(u),math.cos(v)*math.sin(u),math.sin(v)))
        points.append(row);normals.append(normal)
    for i in range(64):
        for j in range(24):
            q=[points[i][j],points[i+1][j],points[i+1][j+1],points[i][j+1]]
            n=normals[i][j]
            light=max(0,n[0]*-.38+n[1]*-.5+n[2]*.75)
            color=f'hsl({66+light*6:.1f},{44+light*21:.1f}%,{26+light*42+light**14*19:.1f}%)'
            pts=' '.join(f'{x:.1f},{y:.1f}' for x,y,z in q)
            faces.append((sum(p[2] for p in q)/4,f'<polygon points="{pts}" fill="{color}" stroke="#26310c" stroke-opacity=".16" stroke-width=".65"/>'))
    faces.sort(key=lambda f:f[0])
    svg='<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 640">'+''.join(f[1] for f in faces)+'</svg>'
    (ROOT/'assets/intelligence.svg').write_text(svg)

if __name__=='__main__':build()
