
import javax.xml.bind.annotation.XmlRootElement;
import java.io.Serializable ;
@XmlRootElement
public class Etudiant {
    private int identifiant ;
    private String nom;
    private double moyenne;

    public Etudiant() {
    }

    public Etudiant(int identifiant, String nom, double moyenne) {
        this.identifiant = identifiant;
        this.nom = nom;
        this.moyenne = moyenne;
    }

    public int getIdentifiant() {
        return identifiant;
    }

    public String getNom() {
        return nom;
    }

    public double getMoyenne() {
        return moyenne;
    }

    public void setIdentifiant(int identifiant) {
        this.identifiant = identifiant;
    }

    public void setNom(String nom) {
        this.nom = nom;
    }

    public void setMoyenne(double moyenne) {
        this.moyenne = moyenne;
    }
}


