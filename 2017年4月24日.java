1.给一个词典，找出其中所有最长的单词。
  1.第一个暴力遍历就是先遍历一次找到最大长度,然后第二次遍历找最大长度的所有单词.
  2.为了只遍历一次,这里运用贪新算法的思想,找到当前的遍历过的最大长度单词,并将等长的单词存入,一旦发现更长的单词,把容器清空,然后继续遍历.
    class Solution {  
        /** 
         * @param dictionary: an array of strings 
         * @return: an arraylist of strings 
         */  
        ArrayList<String> longestWords(String[] dictionary) {  
           
            ArrayList<String> list = new ArrayList<String>();  
            if(dictionary==null){  
                return null;  
            }else{  
                int len=0;  
                for (int i = 0; i < dictionary.length; i++) {  
                    if(dictionary[i].length()>len){  
                        list.clear();  
                        list.add(dictionary[i]);  
                        len=dictionary[i].length();  
                        continue;  
                    }  
                    if(dictionary[i].length()==len){  
                        list.add(dictionary[i]);  
                    }  
                }  
            }  
            return list;  
          
        }  
    };  
