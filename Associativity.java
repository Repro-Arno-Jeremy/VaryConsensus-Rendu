public class Associativity {
    private double x;
    private double y; 
    private double z;

    public Associativity(){
        x = Math.random();
        y = Math.random();
        z = Math.random();
    }

    public static void main(String[] args){
        int equals = 0;
        for(int i=0 ; i<1000 ; i++){
            Associativity a = new Associativity();
            if((a.x + a.y) + a.z == a.x + (a.y + a.z)){
                equals++;
            }
        }
        System.out.println("Fraction de bonnes réponses : " + equals + " sur 1000");
    }
}
