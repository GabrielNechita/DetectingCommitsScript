# DetectingCommitsScript

Am realizat in cadrul laboratorului de Administrarea Sistemelor de Operare un script care ruleaza in interiorul unei masini virtuale pe care am instalat Linux si sistemul de versionare GitLab.

Scriptul realizeaza urmatoarele cerinte:
- Verifica periodic (odata la 30 de secunde) daca exista commituri noi folosind comenzile git add . si git commit
- In cazul in care exista un commit nou se ruleaza comanda de build make dând si locatia fisierului makefile
- In cazul in care buildul a reusit, se copiaza binarele rezultate intr-un alt folder de pe sistem, ce va contine cate un subfolder pentru fiecare versiune noua, de forma build_N, unde numarul versiunii N se incrementeaza automat
