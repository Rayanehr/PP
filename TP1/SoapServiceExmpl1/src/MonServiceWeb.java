import javax.jws.WebMethod;
import javax.jws.WebParam;
import javax.jws.WebService;

@WebService(targetNamespace = "http://www.polytech.fr")
public class MonServiceWeb {
    @WebMethod(operationName = "convertir")
    public double conversion (double mt) {
        return mt*0.9 ;
    }
    public double somme (@WebParam(name = "WebParam1")double a, double b) {
        return a+b;
    }

    public Etudiant getEtudiant (int identifiant) {
        return new Etudiant(1,"Mario", 19);
    }
}
