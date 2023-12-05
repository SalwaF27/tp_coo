#include <iostream>
#include <cpr/cpr.h>
#include <curl/curl.h>
#include <nlohmann/json.hpp>

using namespace std;
using json = nlohmann::json;

class Departement
{
    int _numero;
    double _prixparMcarre;


public:

//constructeur Departement
	    Departement(int n, double p):_numero{n}, _prixparMcarre{p} {}
	    
//un constructeur prenant un paramètre json data
	    Departement(const json& data)
	    {
	      _numero=data["numero"];
	      _prixparMcarre=data["prixparMcarre"];
	      
	    }
	    
//un constructeur prenant un paramètre int id
	   Departement(int depId)
	   {
	   // Requête HTTP 
	   string UrlDep ="http://localhost:8000/departement/"+to_string(depId);
	   cpr::Response r = cpr::Get(cpr::Url{UrlDep},cpr::Authentication{"sch", "sch123456789", cpr::AuthMode::BASIC});
	  
		  //Affichages des informations 
		  std::cout << r.url << std::endl;
		  std::cout << r.status_code << std::endl;
		  std::cout << r.header["content-type"] << std::endl;
		  //Parsez le texte JSON
		  
		  std::cout << r.text << std::endl;
		   
		  try
		    {
		        json data = json::parse(r.text);
			_numero=data["numero"];
	      		_prixparMcarre=data["prixparMcarre"];
			afficher(std::cout );
			 std::cout << std::endl;
		     
		    }
		    catch (const json::parse_error& e)
		    {
			std::cout << e.what() << std::endl;
		    }

		   
		    json j = json::parse(r.text, nullptr, false);

		    if (j.is_discarded())
		    {
			std::cout << "the input is invalid JSON" << std::endl;
		    }
		    else
		    {
			std::cout << "the input is valid JSON: " << j << std::endl;
		    }

		}
		
//affichage de classe departement
void afficher(std::ostream & flux)
	const {
		    flux << "Departement:" << _numero << "," << _prixparMcarre ;
	      }

};


class Ingredient
{
	string nom_ing;
	
 public:
 	Ingredient(string nom)
 	{
 		nom_ing= nom;
 	}
 	
 	
 	Ingredient(json Ing)
 	{
 		nom_ing= Ing["nom"];
 	}
 	
 	Ingredient(int IngId)
 	{
 		 // Requête HTTP 
	   string UrlIng ="http://localhost:8000/ingredient/"+to_string(IngId);
	   cpr::Response r = cpr::Get(cpr::Url{UrlIng},cpr::Authentication{"sch", "sch123456789", cpr::AuthMode::BASIC});
	  
		  //Affichages des informations 
		  std::cout << r.url << std::endl;
		  std::cout << r.status_code << std::endl;
		  std::cout << r.header["content-type"] << std::endl;
		  //Parsez le texte JSON
		  
		  std::cout << r.text << std::endl;
		   
		  try
		    {
		        json data = json::parse(r.text);
			nom_ing= data["nom"];
			afficher(std::cout );
			std::cout << std::endl;
		     
		    }
		    catch (const json::parse_error& e)
		    {
			std::cout << e.what() << std::endl;
		    }

		   
		    json j = json::parse(r.text, nullptr, false);

		    if (j.is_discarded())
		    {
			std::cout << "the input is invalid JSON" << std::endl;
		    }
		    else
		    {
			std::cout << "the input is valid JSON: " << j << std::endl;
		    }

		}
 void afficher(std::ostream & flux)
	const {
		    flux << "Ingredient:" << nom_ing ;
	      }
 	
 	
};


int main(int argc, char** argv)
{

	 // Departement hg(31,2000);
	  Departement HauteGaronne(1);
	  
	  
	  Ingredient orge(2);
	
	  	

return 0;
};
