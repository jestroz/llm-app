#!/bin/bash
#
if [[ ! $1 ]];then
	echo "Falta pasar modelo a crear"
	exit 1
fi

function copy_run() {
	echo "Crear modelo de Ollama basado en Modelfile...."
	echo -n "Continuar si/no: "
	read cont
	if [[ $cont == 'si' ]]; then
		model_name=$1
		docker exec -it ollama ollama stop ${model_name}
		docker exec -it ollama ollama rm ${model_name}
		docker cp Modelfile_${model_name} ollama:/root
		docker exec -it ollama ollama create ${model_name} -f /root/Modelfile_${model_name}
		docker exec -it ollama ollama list
	else
		exit 0
	fi
}

function run_app() {
	echo
	echo "Build de contenedor docker con codigo...."
	echo -n "Continuar si/no: "
	read cont
	if [[ $cont = 'si' ]]; then
		docker build . -t llm-app
		docker run --rm -it llm-app python app.py
	else
		exit 0
	fi
}

copy_run $1
run_app
