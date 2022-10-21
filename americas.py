import pygal

mm = pygal.maps.world.World()
mm.title = 'North, Central  and Sount America'

mm.add('North America', ['ca', 'mx', 'us'])
mm.add('Central America', ['bz', 'cr', 'gt', 'hn', 'ni', 'pa', 'sv'])
mm.add('Sount America', ['ar', 'bo', 'br', 'cl', 'co', 'ec', 'gf', 'gy', 'pe',
 'py', 'sr', 'uy', 've'])

mm.render_to_file('americas.svg')