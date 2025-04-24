import java.io.*;
import java.util.*;

/*

Find the start/end of the journey given list of boarding passes

A ---------->C----------->D----------->E-----------> B

Boarding passes in order (start city -> end city)
A->C
C->D
D->E
E->B

Actual random input for this problem

D->E
A->C
C->D
E->B

Desired output (start city -> final city)
A -> B

*/
class BP  
{
   public String start;
   public String end;

   public BP(String start, String end)
   {
    this.start = start;
    this.end = end;
   }
}

class BoardingPassSolution {
  public static void main (String args[]){
    List<BP> bppasses = new ArrayList<>();

    bppasses.add(new BP("D", "E"));
    bppasses.add(new BP("A", "C"));
    bppasses.add(new BP("C", "D"));
    bppasses.add(new BP("E", "B"));

    getJourneyInfo(bppasses);
  }
  
  private static String findFirstElemInAButNotInB( Set<String> A, Set<String> B ) {
    for ( String keyA : A ) {
      if ( !B.contains( keyA )) {
   	return keyA;  
      }
    }
    return null;
  }

  private static void getJourneyInfo(List<BP> passes)
  {

    Set<String> setStart =new HashSet<>(); 
    Set<String> setEnd =new HashSet<>();
    for (int i =0; i < passes.size(); i++ ) {
      BP bp =passes.get(i);
      setStart.add( bp.start);
      setEnd.add(bp.end);
    }

    String startNode =findFirstElemInAButNotInB( setStart , setEnd ) ;
    String endNode =findFirstElemInAButNotInB( setEnd, setStart );
   
    BP soln =new BP( startNode, endNode );
    System.out.println( soln.start +"-->"+ soln.end);
  }
}
