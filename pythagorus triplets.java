
  
  public class Main{
  
  public static void main(String[] args) {
    Scanner scn= new Scanner(System.in);
    int base=scn.nextInt();
    int height=scn.nextInt();
    int hypo=scn.nextInt();
    
    
    int max=0;
    if(hypo>base && hyop>height)
    {
        max=hypo;
        
    }
    else if(base>hypo && base>height)
    {
        max=base;
        
    }
    
    else
    {
        max=height;
        
    }
    
    if(max==base)
    {
        System.out.println(base*base=height*height+hypo*hypo);
        
        
        
    }
    
    else if(max==hypo)
    {
        System.out.println(hypo*hypo=height*height+ base*base);
        
    }
    
    else
    {
        System.out.println(height*height=base*base+hypo*hypo);
        
    }
   }
  