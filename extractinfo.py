import googlesearch
import webbrowser as wb

def opengoogle(query):
    try:
        from googlesearch import search
    except ImportError:  
        print("No module named 'google' found") 
  
    # to search 
    #query = "dilber"

    listj = []
    for j in search(query, tld="co.in", num=10, stop=1, pause=2): 
        listj.append(j)
        #print(j)

    #print(listj)
    url = ''
    for i in listj:
        if('www.youtube.com/watch?v=' in i):
            #print(i)
            url = i

    wb.open(url)

#opengoogle('ignite official song')
