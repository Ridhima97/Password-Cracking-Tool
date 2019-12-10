#define _XOPEN_SOURCE 
#include <stdio.h>
#include <unistd.h>
#include <string.h>


int main() {
	FILE *wordlist;
	//char *hash;
	/* if(num < 2) {
		printf("Error");
		return 1;
	} */ 

	//int n = strlen(args[1]);
	//int n=40;
	
	/*for(int i =0; i<n; i++) {
		word[i] = args[1][i];
	} */
	char pass[41] = "00000273b52ee943ab763d2bb3d83f5dc3d30904"; 

	char salt[3];
	char word[41];
	salt[0] = pass[0];
	salt[1] = pass[1];
	salt[2] = '\0'; //terminate string
	wordlist = fopen("/Users/ridhimaagarwal/Downloads/english.txt", "r");

	while(fgets(word,41,wordlist)!= NULL) 
	{  
		//printf("test1");
		if(!strcmp(pass, crypt(word,salt)))
		{
			printf("Password Found: %s  %s\n", pass, word);
			return 0;
		}
	}
	printf("List done/not found\n");
	fclose(wordlist);
	return 0; 
}
