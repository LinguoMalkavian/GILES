import urllib2
from bs4 import BeautifulSoup
import re

def form(ans):
    ans= re.sub(r"<.*?>"," ",ans)
    ans=re.sub(r"\(.*?\)"," ",ans)
    ans= re.sub(r"\s+"," ",ans)
    ans=ans.strip()
    
    return ans

def main():
    direct="Data/"
    #Change extracting characters here
    charlist=["ANGEL","SPIKE","CORDELIA","ANYA"]


    for numep in range(1,2):
        folder=direct+"fulleps"+"/"
        masterfile=file(folder+"episode%d"%numep+".txt","w")
        charfiles={}
        for char in charlist:
            charfiles[char]= file(direct+char+"/"+char+"ep"+str(numep)+".txt","w")
        
        #get the page and build the soup
        url="http://buffyworld.com/buffy/scripts/%03d_scri.html"%numep
        page=urllib2.urlopen(url).read()
        soup=BeautifulSoup(page)
        #get centered blocks
        dialogue=soup.find_all('center')
        lines=[]
        for chunk in dialogue:
            #process each centered block containing dialogue
            text=str(chunk)
            lines+=re.findall(r"([A-Z]+)<br\/?>(.*?)<\/?p>", text,re.DOTALL)
            
        for line in lines:
            #turn the line part into printable format by ridding it of html tags and linebreaks
            printable= form(line[1])
            #write the line into the episode script
            masterfile.write(line[0]+"\t"+ printable + "\n")
            charname=line[0].strip().upper()
            if charname in charlist:
                #write the line into the Character's script
                charfiles[charname].write(printable+"\n")
        print "Done with episode: %d"%numep
        masterfile.close()
        for char in charfiles:
            charfiles[char].close()

    print "Done"

main()
