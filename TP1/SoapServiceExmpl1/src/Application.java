import javax.xml.ws.Endpoint;

public class Application {
    public static void main(String[] args) {

        System.out.println("Debut de deploiment de mon service");
        String url = "http://localhost:8080/C:8080/";
        Endpoint.publish(url, new MonServiceWeb());
        System.out.println("Le service web est déployé");
        }
    }
