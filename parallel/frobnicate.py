#!/usr/bin/python

import sys
import random
import time

'''
Usage: ./frobnicate.py <word> <iterations> <scale>

This script just iterates through a loop <iterations> times printing
a formatted outputline of nonsense and then sleeps random.random() * <scale>
'''

lorem = '''Lorem ipsum dolor sit amet, consectetur adipiscing elit.
Pellentesque sit amet nibh cursus lacus scelerisque commodo.
Duis et sapien sollicitudin, pretium sapien eu, vehicula risus.
Nunc vel purus quis leo aliquam semper in commodo mauris.
Suspendisse scelerisque risus hendrerit lectus luctus, nec lobortis massa luctus.
Sed aliquam quam ut pulvinar ornare.
Sed viverra enim quis elementum porta.
Mauris vitae odio mollis, porta nibh laoreet, tempus diam.
Donec sollicitudin eros non ultrices semper.
Integer elementum ante quis nibh egestas varius.
Quisque vitae tellus non sem dapibus pellentesque vitae sit amet massa.
Vestibulum in metus at nulla vestibulum posuere at condimentum sapien.
Quisque dapibus neque et libero vehicula faucibus.
Vivamus malesuada lorem ac turpis bibendum, vehicula viverra mi bibendum.
Etiam ornare erat a ligula ultrices auctor.
Pellentesque tempus justo ut euismod tincidunt.
Etiam fringilla tellus at viverra tincidunt.
Aenean adipiscing ipsum at odio pulvinar semper.
Fusce semper lacus at arcu scelerisque, id hendrerit erat tristique.
Donec malesuada odio in accumsan rhoncus.
Pellentesque ac arcu tempor, viverra lorem vel, rutrum purus.
Aenean vitae lectus suscipit, egestas est tempus, interdum magna.
Praesent vel ante sit amet lorem aliquet faucibus.
Aliquam fermentum est laoreet dignissim tempus.
Sed interdum turpis sit amet metus tincidunt feugiat.
Morbi volutpat tortor vel ligula adipiscing feugiat.
Nunc faucibus urna eu bibendum bibendum.
Nam dignissim sapien id urna cursus rhoncus.
Duis rhoncus dolor et lectus luctus, quis volutpat ligula placerat.
Nam et elit molestie, consequat velit in, sollicitudin nisl.
Vivamus vestibulum magna a vehicula vulputate.
Praesent tincidunt eros eu est hendrerit, a venenatis odio tristique.
Curabitur ut nisi ultrices, condimentum lorem non, egestas nibh.
Mauris consectetur neque porta quam mollis sagittis.
Suspendisse eget felis eget felis pharetra ultricies.
Sed rutrum nisi a est accumsan adipiscing.
Sed in dui ut dolor aliquam bibendum.
Donec volutpat massa sit amet porta aliquet.
Proin eu massa aliquet, lobortis sapien ut, porta nibh.
Nunc vel tellus non felis varius vestibulum et ut est.
Etiam sit amet quam quis ligula suscipit gravida eu in turpis.
Etiam blandit felis a posuere convallis.
Mauris quis elit sed nisl adipiscing interdum vitae eu dui.
Donec nec tortor pellentesque odio ultrices tincidunt.
Donec imperdiet odio quis volutpat consectetur.
Vivamus adipiscing purus ac est convallis, at auctor massa imperdiet.
In quis nisl viverra, suscipit lectus sed, viverra lorem.
Praesent ac ligula euismod, porta ligula in, tincidunt justo.
Ut in tellus ut tellus scelerisque vulputate.
Cras auctor erat ac ante viverra ullamcorper.
In id justo cursus, elementum felis a, tincidunt elit.
Suspendisse sodales erat imperdiet quam mollis suscipit.
Fusce et odio id nibh accumsan euismod.
Morbi quis sapien fermentum, aliquet arcu ac, rutrum ante.
Suspendisse eu urna fermentum, consequat sapien non, gravida turpis.
Cras et nulla fringilla justo viverra interdum.
Pellentesque accumsan nibh ac magna tincidunt, dapibus ornare arcu aliquam.
Donec mollis magna et est scelerisque pulvinar.
Sed luctus lectus eget cursus mattis.
Vivamus molestie dolor vel nisi pharetra ultrices.
Mauris aliquet ligula porta, ullamcorper dolor vitae, tempus mauris.
Morbi sit amet dolor gravida, commodo arcu ac, dapibus ante.
Nam vitae magna lobortis nisl vestibulum rutrum at condimentum tortor.
Praesent scelerisque tortor sed elit laoreet ultrices.
Praesent condimentum turpis rhoncus pellentesque pulvinar.
Donec sed augue id lectus adipiscing malesuada eu nec libero.
Etiam varius erat non facilisis porta.
Sed commodo metus ac turpis mattis hendrerit.
Etiam nec libero sed dui feugiat congue.
Fusce ultrices nisi vel ligula varius tincidunt.
Sed sed ipsum ut risus consectetur aliquet a in sapien.
In sed nunc vitae lectus facilisis pulvinar non et nulla.
Nam pharetra massa et erat ullamcorper, vitae lobortis ligula porttitor.
Etiam id risus id diam tristique volutpat.
Proin sit amet dolor non velit tincidunt suscipit.
Donec mattis odio vitae scelerisque tempus.
Vestibulum a quam nec tortor mollis laoreet sed nec enim.
Fusce ultrices dolor eu ornare eleifend.
Vivamus id nisl sagittis, elementum nisi nec, mollis metus.
Duis ut justo ac massa porta feugiat.
Praesent in turpis facilisis, tempus dui et, aliquam eros.
Fusce facilisis est et orci porta, quis vulputate purus venenatis.
In placerat dui egestas convallis mattis.
Nulla gravida nibh non velit laoreet convallis.
Fusce rhoncus sem ut mauris sodales rhoncus.
Ut lobortis velit at orci gravida, sed luctus augue imperdiet.
Nunc lacinia tellus ac sapien dignissim pellentesque.
Curabitur placerat mauris at sem sagittis, id hendrerit odio pharetra.
Vivamus porttitor lorem consequat, aliquet nisi sed, feugiat massa.
Sed non est et libero viverra dignissim varius ut sapien.
Fusce viverra lorem in arcu eleifend, at fringilla metus consectetur.
Donec non sem nec leo vulputate condimentum non ut quam.
Praesent quis enim vitae dui commodo blandit nec a metus.
Fusce cursus nisi sit amet urna porta condimentum.
Nullam imperdiet mi in elit accumsan, non ullamcorper ligula porttitor.
Vestibulum molestie metus eget purus viverra consectetur.
Phasellus aliquam ante et viverra faucibus.
Nam id ligula et arcu aliquet aliquam sed at risus.
Integer pellentesque massa sit amet commodo accumsan.
Maecenas aliquet lorem eu justo lobortis, tincidunt egestas mi egestas.
Nulla ultricies dolor varius vestibulum vestibulum.
Nunc pellentesque purus eu dignissim egestas.
Cras non ante malesuada, vehicula arcu eu, faucibus metus.
Nullam viverra nisi vel purus hendrerit, venenatis adipiscing diam porta.
Nulla ut orci sit amet lacus blandit luctus.
Maecenas eget metus in diam pellentesque ullamcorper.
Vestibulum blandit sapien at purus sodales, eu pulvinar massa tempor.
Suspendisse imperdiet felis ac justo pulvinar iaculis.
Vivamus condimentum dolor non ligula rutrum consectetur.
Proin nec massa mattis, molestie nisi malesuada, laoreet tortor.
Etiam vestibulum magna vitae augue commodo, nec ullamcorper leo ornare.
Ut vestibulum leo nec ligula interdum pretium.
Praesent eget nibh quis nibh pulvinar pharetra.
Vivamus ac libero et mauris facilisis porttitor ut non eros.
Aenean dignissim est ac leo vestibulum faucibus.
Pellentesque at dolor quis lorem lacinia rhoncus.
Proin ornare sem vitae pellentesque fringilla.
Curabitur quis purus accumsan, laoreet tellus vitae, faucibus mi.
Quisque blandit velit ac erat iaculis, ac vestibulum mauris aliquet.
Mauris non nulla vitae quam convallis vulputate a vel metus.
Morbi id ligula vel eros rhoncus accumsan non vel lorem.
Ut feugiat nisl sit amet sem scelerisque convallis.
Donec id lacus ac dui fringilla viverra.
Cras a dolor tristique, tempus lectus vitae, sodales lacus.
Donec non libero ultrices tortor tempus mattis eu et orci.
Suspendisse eget nibh sed enim porta sodales.
Sed vel lorem dignissim, congue nisi in, lacinia quam.
Donec non tortor eleifend, fringilla tortor ac, ullamcorper mi.
Sed fringilla eros varius laoreet volutpat.
Aenean tempor est quis arcu imperdiet, non iaculis sapien lacinia.
Phasellus sit amet ligula id lectus laoreet tincidunt.
Curabitur pellentesque nulla non magna imperdiet euismod.
Etiam pulvinar est at metus porttitor elementum.
Curabitur pharetra elit eu scelerisque egestas.
Nulla in mi eget magna semper vehicula.
Aliquam non purus vel elit auctor facilisis.
Mauris ut libero in odio mollis fermentum eu sit amet orci.
Ut vitae nulla sit amet tellus eleifend commodo.
Phasellus imperdiet ipsum imperdiet nisl vulputate porttitor nec ut dolor.
Aliquam vel risus sit amet metus condimentum volutpat.
Nulla ornare justo vel nibh tempor ullamcorper.
Quisque elementum elit non lorem pharetra, sit amet vulputate felis mollis.
Praesent pharetra dui sit amet massa sagittis imperdiet.
In iaculis mauris non consequat ultricies.
Aliquam imperdiet neque vitae lorem scelerisque cursus.
Donec eu lacus accumsan, interdum neque sed, pellentesque tellus.
Nullam rhoncus nibh nec auctor volutpat.
Nunc blandit mi a neque tempus, sit amet gravida turpis malesuada.
Nulla hendrerit velit quis dui ultrices imperdiet.
Proin rhoncus mauris at fringilla fringilla.
Nulla interdum libero eget egestas imperdiet.
Suspendisse vel ligula faucibus, tincidunt metus vitae, mattis est.
Integer non risus ac dolor pellentesque cursus in aliquam orci.
Quisque fermentum lectus a nibh porta, in tincidunt sapien elementum.
Proin nec tortor sit amet massa imperdiet consectetur quis at diam.
Nullam quis libero viverra, cursus tortor quis, dictum magna.
Morbi at urna nec magna faucibus vestibulum sed non erat.
Morbi auctor risus vitae nibh imperdiet faucibus.
Sed at quam in mi posuere convallis.
Curabitur ac odio vitae urna laoreet porttitor vitae id turpis.
Mauris accumsan est ut ultricies sollicitudin.
Fusce sollicitudin erat sed auctor interdum.
Quisque pharetra sem vitae sem blandit, nec consequat ipsum ornare.
Aenean vehicula turpis eu semper varius.
Vivamus posuere nibh non malesuada ornare.
Phasellus aliquet nunc sed diam tempus lobortis.
Mauris mollis lacus a feugiat adipiscing.
Nunc a mauris vel nibh varius vehicula.
Sed bibendum augue vitae venenatis semper.
Donec non sem eget nisl bibendum porta vel id nisi.
Nullam faucibus lectus nec lorem consequat tempor.
Ut et turpis sodales odio pretium volutpat.
Morbi ut ipsum dignissim urna lobortis gravida.
Phasellus in magna id turpis ultricies pellentesque.
Curabitur id nunc a mi rutrum pellentesque nec a mauris.
Nulla eget metus lobortis, mattis odio ac, semper est.
Etiam tristique neque nec mauris convallis, consequat rhoncus eros ornare.
Sed interdum elit ac varius auctor.
Quisque tempus ipsum id iaculis rhoncus.
Sed eu sem eu lectus tristique sodales.
Proin vitae mauris eget justo tempus adipiscing cursus nec ligula.'''.split('\n')

def main():
    word = sys.argv[1]
    iters = int(sys.argv[2])
    scale = int(sys.argv[3])

    print "frobnicating '%s' %d times about every %d seconds" % (word, iters, scale)
    for i in range(1,iters + 1):
        print "[%s-%03d]: %s" % (word, i, random.choice(lorem))
        time.sleep(random.random() * scale)

if __name__ == '__main__':
    main()
