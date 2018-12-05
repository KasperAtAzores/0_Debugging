import bpy

from random import uniform
from math import cos, sin, radians, pi

# The next functions are for building gems in the style of this one    
# https://www.vector-eps.com/wp-content/gallery/diamong-geometric-shapes-vector/thumbs/thumbs_diamong-geometric-shapes-vector5.jpg
def gemstone_mesh_top(name, final_height, location, material):
    # returns a set of angles corresponding to dividing the circle in N, and shifting 
    # all clockwise with an offset (in degrees)
    def split_circle(N, offset=0):
        return [ radians(a+offset) for a in range(0,360, int(360/N) )]

    # computes an index based on a cyclus of N, and offset
    def mod(a, N,offset):
        return (a % N) + offset
    r0 = 2 # top
    r1 = 3
    r2 = 4
    r3 = 2
    h = 6.2
    # top
    verts = [(cos(v)*r0, sin(v)*r0, h) for v in split_circle(6)]
    # middle upper part
    verts.extend( [(cos(v)*r1, sin(v)*r1, h-1) for v in split_circle(6,30)] )
    # upper band
    verts.extend( [(cos(v)*r2, sin(v)*r2, h-2) for v in split_circle(12)] )
    # lower band
    verts.extend( [(cos(v)*r2, sin(v)*r2, h-2.2) for v in split_circle(12)] )
    # middle lower part
    verts.extend( [(cos(v)*r3, sin(v)*r3, 2) for v in split_circle(6,30)] )
    verts.append( (0,0,0) )
    # top face
    faces = [[ a for a in range(0,6) ]]
    # six triangles
    faces.extend( [ [a,a+6,(a+1)%6] for a in range(0,6)] )
    # six quadrilaterals
    faces.extend( [ [mod(a+1,6,0), mod(a,6,6), mod(2*a+2, 12, 12), mod(a+1,6,6) ] for a in range(0, 6)] )
    # twelve triangles
    faces.extend( [ [mod(a,12,12), mod(a+1,12,12), mod( int(a/2),6,6)] for a in range(0,12)] )
    # twelve small rectangles - the band
    faces.extend( [ [mod(a,12,24), mod(a+1,12,24), mod(a+1,12,12), mod(a,12,12)] for a in range(0,12)] )
    # twelve rectangles below the band
    faces.extend( [ [mod(a,12,24), mod(int(a/2),6,36), mod(a+1,12,24) ] for a in range(0,12)] )
    # final six quadrilaterals
    faces.extend( [ [mod(a,6,36), 42, mod(a+1,6,36), mod(a*2+2,12,24) ] for a in range(0,6) ] )
    me = bpy.data.meshes.new('gemstone_mesh')
    me.from_pydata(verts, [], faces)
    ob = bpy.data.objects.new(name, me)
    scale = final_height/h
    ob.scale = ( scale, scale, scale )
    ob.location = location
    bpy.context.scene.objects.link(ob)
    ob.select = True
    #ob.active_material = material
    ob.data.materials.append( material )
    bpy.context.scene.objects.active = ob
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    
    
# make a material for the gems, or retun an existing if one exist with the 
# given name
def gem_material(name, rgb_color):
    if name in bpy.data.materials:
        print("Got material: " + name)
        return bpy.data.materials[name]
    mat = bpy.data.materials.new(name)
    mat.diffuse_color = rgb_color
    mat.use_transparency = True
    mat.alpha = 0.9
    mat.emit = 0.5
    return mat

def ruby(location, size=1):
    ruby_mat = gem_material( 'ruby_material', (0.8, 0.15, 0.15))
    gemstone_mesh_top('ruby',size, location, ruby_mat)
    
def emerald(location, size=1):
    emerald_mat = gem_material( 'emerald_material', (0.15, 0.8, 0.15))       
    gemstone_mesh_top('emerald',size, location, emerald_mat) 

def make_gems(no_ruby, no_emerald, area):
    bpy.ops.object.select_all(action='DESELECT')
    for i in range(no_ruby):
        x = uniform(-area+5, area-5)
        y = uniform(-area+5, area-5)
        ruby( (x,y, 4), 2)
    for i in range(no_emerald):
        x = uniform(-area+5, area-5)
        y = uniform(-area+5, area-5)
        emerald( (x,y, 4), 2)
    bpy.ops.object.select_all(action='DESELECT')
