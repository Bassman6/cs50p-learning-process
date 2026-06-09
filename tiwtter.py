def main():
    users_input = input("world: ")
    print(shorten(users_input))






def shorten(word):
    #z = ["a,e,i,o,u,A,E,I,O,U"]
    vowels = "aeiouAEIOU"
    for i in vowels:
        
        word = word.replace(i,"")
        
    return word
        




if __name__ == "__main__":
    main()
