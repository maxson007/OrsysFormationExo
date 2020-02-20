http://pythontutor.com/

https://pyformat.info/

https://regexper.com/

http://buildregex.com/

https://regex101.com/

regex nom prenom: `^[a-zA-Z]+[ \-']?[[a-zA-Z]+[ \-']?]*[a-zA-Z]+$`

regex numero de telephone: `^[+]?[0-9]{,15}$`

regex email: `^[a-z0-9._+-]+@[a-z0-9.-]+\.[a-z]{2,}$`


Mysql database: 
```
CREATE TABLE contact(
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nom  VARCHAR(100),
    prenom  VARCHAR(100),
    numerotel  VARCHAR(100),
    email  VARCHAR(100)
);
```
