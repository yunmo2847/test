import folium
p= [[36.51141100904502, 127.26227785356602],[36.50974805976162, 127.26286419903644],[36.51098406422511, 127.2640890315588]]
m = folium.Map(location=p[0],zoom_start=40)
for i in range(len(p)):
        folium.Marker(location=p[i]).add_to(m)













m.save("map.html")

