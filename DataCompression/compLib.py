try :
    from collections import Counter 
    import sys
except e :
    print(e)

class compLib:
    def __init__(self) :
        pass 
    
    def count_occurence(self,mots):
        all_unique_word = ''.join(set(mots))
        c = Counter(mots)
        all_unique_word_with_lenght = {}
        for m in all_unique_word :
            r = all_unique_word_with_lenght
            r[m] = c[m]
            r = r[m]
        return all_unique_word_with_lenght
    
    def sort_dict(self,dic):
        from operator import itemgetter
        sorted_dict = {}
        for i in sorted(dic.items(), key=itemgetter(1)) :
            sorted_dict[i[0]] = i[1]
        return sorted_dict
    
    def build_huffman_tree(self,list_word):
        s_total = list_word.values()
        huffman_tree = {}
        lw = list_word
        while len(lw) > 1  :
            ht = huffman_tree
            i = 0
            key_min = []
            sum_min_key = 0
            if len(lw) < 2 :
                i = 1
            while i < 2 :
                min_k = min(lw.keys(), key=(lambda k: lw[k]))
                key_min.append( min_k )
                sum_min_key = sum_min_key + lw[min_k]
                #print(lw)
                del lw[min_k]
                i+=1
            ht[''.join(key_min)] = key_min
            ht = ht[''.join(key_min)]
            lw[''.join(key_min)] = sum_min_key
        return huffman_tree
    
    #Mamadika an ilay Tree ho binary code amzay 
    def read_Huffman_Tree(self,e,Tree,list_word):
        code = ''
        for n in Tree :
            if e in Tree[n] :
                if Tree[n].index(e) == 0 :
                    code += str(0)
                else:
                    code += str(1)
                e = n
        code = code[::-1]
        return code 
    
    def Huffman_compress(self,data):
        code_huff = ''
        Tree = self.build_huffman_tree(sort_dict(count_occurence(str(data))))
        list_unik = sort_dict(count_occurence(str(data)))
        final_array = dict()
        for e in list_unik :
            code_huff= self.read_Huffman_Tree(e,Tree,list_unik) 
            final_array[e] = code_huff
        final_code = ''
        for d in data :
            final_code = final_code + final_array[d]
        #f_code = code_bin(final_code)
        return Tree , final_code ,final_array
    
    def decode_Huffman(self,Tree,Huffman_code):
        H_code = Huffman_code
        #H_code = to_bin(Huffman_code)
        root = list(Tree.keys())[-1]
        decoded_text = ''
        for c in H_code :
            c = int(c)
            current_node = Tree[root]
            if current_node[c] in Tree :
                root = current_node[c]
            else :
                decoded_text+=current_node[c]
                root = list(Tree.keys())[-1]
                    
        return decoded_text
    
    #re compress binary file from huffman 
    def code_bin(self,Hc):
        Hc+='E'
        redundancy = 1
        coded_bin = Hc[0]
        for i,b in enumerate(Hc) :
            if i+1 < len(Hc) :
                if Hc[i] == Hc[i+1] :
                    redundancy+=1
                else :
                    coded_bin+=str(redundancy)
                    redundancy = 1
            
        return coded_bin

    def to_bin(self,codedbin):
        begin = codedbin[0]
        binary = begin
        i=1
        while i < len(codedbin):
            binary += str(codedbin)*i
            reverse = lambda x : '0' if x == '1' else '1'
            begin = reverse(binary)
            i+=1
        return binary
    

    