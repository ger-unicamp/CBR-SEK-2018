#include<stdio.h>

#define MAX 3

int pos=1;
char leitura_sensor = 'B';
char direcao = 'E';
struct pilha{
	char cor;
	char dir;
};
struct pilha estagio[MAX];
typedef struct pilha pilha;

void push(char corpush, char dirpush);
void pop();

int main(){
	while(1){
		while(leitura_sensor == 'B'){
			//funcao que le o sensor e converte a medida em cores
		}
		push(leitura_sensor,direcao);
	}
}

void push(char corpush,char dirpush){
	if(pos == MAX){
		printf("FIM DA PILHA\n");
	}
	else{
		estagio[pos].cor = corpush;
		estagio[pos].dir = dirpush; 
		pos++;
	}
}
void pop(){
	if(pos == 1){
		printf("FIM DA PILHA\n");
	}
	else{
		pos--;
		printf("COR: %c, DIRECAO: %c\n",estagio[pos].cor,estagio[pos].dir);
		estagio[pos].cor = NULL;
		estagio[pos].dir = NULL;
	}
}

