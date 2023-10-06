#include <iostream>
#include <cpr/cpr.h>
#include <curl/curl.h>
#include <nlohmann/json.hpp>
using namespace std;
using json = nlohmann::json;

class Departement
{
    int _numero;
    int _prixparMcarre;

public:
    Departement(int n, int p):_numero{n}, _prixparMcarre{p} {}
    /*Departement(json data)
    {
      _numero=data._numero;
      _prixparMcarre=data._prixparMcarre;
    }
    Departement(int id)
    {
      _numero=id._numero;
    }*/
void afficher(std::ostream & flux)
const {
      flux << "Departement:" << _numero << "," << _prixparMcarre ;
      }

};

int main(int argc, char** argv){
  Departement hg(31,2000);
  cpr::Response r = cpr::Get(cpr::Url{"http://localhost:8000/departement/1"},cpr::Authentication{"sch", "sch123456789", cpr::AuthMode::BASIC});

  std::cout << r.url << std::endl;
  std::cout << r.status_code << std::endl;
  std::cout << r.header["content-type"] << std::endl;
  //std::cout << r.text << std::endl;

  /**/
  try
    {
      json data = json::parse(r.text);

      std::string id = data["id"];
      std::string dep = data["Departement"];
      std::string nep = data["numero"];
      std::string prixparMcarre = data["prixparMcarre"];
      std::cout << dep << '\n';
    }
    catch (const json::parse_error& e)
    {
        std::cout << e.what() << std::endl;
    }

    // parse without exceptions
    json j += json::parse(r.text, nullptr, false);

    if (j.is_discarded())
    {
        std::cout << "the input is invalid JSON" << std::endl;
    }
    else
    {
        std::cout << "the input is valid JSON: " << j << std::endl;
    }
  return 0;
};
