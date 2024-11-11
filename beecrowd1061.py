startday = input().split()
startvalue = int(startday[1])
starthours = input().split(':')
hourstart, minstart, secstart = int(starthours[0]), int(starthours[1]), int(starthours[2])

endday = input().split()
endvalue = int(endday[1])
endhours = input().split(':')
hourend, minend, secend = int(endhours[0]), int(endhours[1]), int(endhours[2])

hoursinsecstart = (hourstart * 3600) + (minstart * 60) + secstart

hoursinsecend = (hourend * 3600) + (minend * 60) + secend 

#resto do dia inicial
reststart = (24 * 3600) - hoursinsecstart

resthour = reststart//3600
restmin = (reststart%3600) // 60
restsec = (reststart%3600) % 60

#resto do dia final
restend = hoursinsecend

resttotal = reststart + restend

resthourtotal = resttotal//3600
restmintotal = (resttotal%3600) // 60
restsectotal = (resttotal%3600) % 60

if resttotal < 86400:
    quantdays = (endvalue - startvalue) - 1
elif resttotal > 86400:
    quantdays = (endvalue - startvalue) + 1
    resthourtotal = (86400 - resthourtotal)//3600

print(f'{quantdays} dia(s)')
print(f'{resthourtotal} hora(s)')
print(f'{restmintotal} minuto(s)')
print(f'{restsectotal} segundo(s)')