class SmallestAndLargest{
  public static String getSmallestAndLargest(String s, int k) {
          String smallest = "";
          String largest = "";

          // Complete the function
          // 'smallest' must be the lexicographically smallest substring of length 'k'
          // 'largest' must be the lexicographically largest substring of length 'k'
          // find all sub strings and compare them

          java.util.TreeSet<String> set = new java.util.TreeSet<>(); 

          for(int i=0;i<=s.length()-k;i++){
              String sub = s.substring(i,i+k);
              set.add(sub);
          }

          smallest = set.first();
          largest = set.last();

          return smallest + "\n" + largest;
      }
}
