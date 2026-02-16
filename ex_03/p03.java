package sowlution_ex3;

import java.util.ArrayList;
import java.util.Random;
/**
 *
 * @author Mhmd rida
 */
public class JackpotMachine {
        ArrayList<String> userNames = new ArrayList<String>();
        Random rand = new Random();
        private String userName;
        private String password;
        private boolean is_signed_n;
        private ArrayList<String> history = new ArrayList<String>();
        private double balance;
        private double plot;
        private int spin;
        
    public JackpotMachine() {
        this.userName = "test";
        this.password = "123";
        this.balance = 0.0;
        this.plot = 0.0;
        this.spin = 0;
        this.is_signed_n = false;
    }
    
    public JackpotMachine(String userName, String password, double balance, int spin) {
        this.userName = userName;
        this.password = password;
        this.balance = 0.0;
        this.plot = 0.0;
        this.spin = 0;
        this.is_signed_n = false;

    }
    
    public void sign_up(String userName , String password) throws Exception
    {
        if (check_if_exists(userName)) {
            throw new Exception("User Name exists :(");
        }
        else
        {
            System.out.println("Signed up :)");
            userNames.add(userName);
            this.is_signed_n = true;
        }
    }
    
    
    public boolean check_if_exists(String userName)
    {
        for (String userName1 : userNames) {     
            if(userName.equals(userName1)) 
            {
                return true;
            }
        }
        return false;             
    } 
    
    public void sign_in(String username, String password) throws Exception
    {
        if (this.userName == null ? username == null : this.userName.equals(username)) {
            if (this.password == null ? password == null : this.password.equals(password)) {
                System.out.println("signed in :)");
                this.is_signed_n = true;
            }
            else{
                throw new Exception("(not) ! signed in :(  -> Incorrect password");
            }
        return ;
        }
        throw new Exception("user Name not found sign up please");        
    }
    
    public void signed_out()
    {
        if (this.is_signed_n == true) {
            System.out.println("signing out ...");
            this.is_signed_n = false;
        }
    }
    
    public void add_to_balance(double amount) throws Exception
    {
        if (amount < 0) {
            throw new Exception("amount can not be -");
        }
        if (is_signed_n) {
            this.balance += amount;
        }
        else
        {
            throw new Exception("please sing in");
        }
    }

    public double view_balance() {
        return balance;
    }
    
    public void spin_jackpot() throws Exception
    {
        if (balance > 10 && is_signed_n) {
            this.balance -= 10;
            this.plot += 10;
            int [] nums = new int[3];
            nums = rand_nums();
            if(nums[0] == 7 && nums[1] == 7 && nums[2] == 7)
            {
                //after spliting and separate the concerns the code should be 
                //person.addbalance((this.amount))
                //history.add("amount: " + amount);
                balance += plot;
                plot = 0.0; 
            }
            else if (nums[0] == 7 && nums[1] == 7 || nums[1] == 7 && nums[2] == 7 || nums[2] == 7 && nums[0] == 7) {
                //after spliting and separate the concerns the code should be 
                //person.addbalance((this.amount)/ 7.0)
                balance +=( plot / 7.0) 
                plot = plot - (plot / 7.0);
                
            }
                   
            if (nums[0] == nums[1] && nums[1] == nums[2]) {
                //after spliting and separate the concerns the code should be 
                //person.addbalance((this.amount / 2.0 ))
                this.balance += (this.amount / 2.0);
                plot = plot / 2;
            }
        }
        else
        {
            throw new Exception("you should have more than 10 coins and be signed in");
        }
    }
    
    public int[] rand_nums(){
        int [] nums = new int[3];
        for (int i = 0; i < nums.length; i++) {
            nums[i] = rand.nextInt(10);
        }
        return nums;
    }
    
    public void view_history() throws Exception
    {
        if (is_signed_n) {
            System.out.print("{");
            for (String hist : history) {
                System.out.print(hist + " ," );
            }
            System.out.println("}");
        }
        else 
        {
            throw new Exception("sign_in!!!!");
        }
    }

}
