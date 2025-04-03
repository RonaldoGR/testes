<script>
import axios from "axios";


export default {
    
  props: {
    msg2023: {
      type: String,
      required: true
    },
  },
    data() {
        return {
            tabela2023: [],
            apiUrl: "http://127.0.0.1:5000/trimestre2023", 
            mostrarDados: false
        };
    },

    methods: {
        getData2023() {
            if (this.mostrarDados) {
                this.mostrarDados = false;
                this.tabela2023 = [];
                return;
            }
            
            axios.get(this.apiUrl)
                 .then(response => {
                  console.log("DADOS: ", response)
                    this.tabela2023 = response.data["TRIMESTRE 2023"];
                    this.mostrarDados = true;
                })
                .catch(error => {
                    console.error("Erro ao buscar os dados: ", error);
                });
            } 
   }
}; 
</script>

<template>
   <section class = container>
        <h2 class="text">{{ msg2023 }}</h2>
        <div>
            <button @click="getData2023">Tabela Trimestre 2023</button>
        </div>
       
        <div>
            <table class ="tabela" v-if="tabela2023.length > 0" border="1">
                <thead class="cabeçalho">
                    <tr>
                        <th>Razão Social</th>
                        <th>Nome Fantasia</th>
                        <th>Despesas</th>
                    </tr>
                </thead>
                <tbody>
                    <tr  v-for="(item, index) in tabela2023" :key="index" >
                        <td>{{ item["Razao Social"] }}</td>
                        <td>{{ item["Nome Fantasia"] || "Não Informado" }}</td>
                        <td>R$ {{ Number(item["Despesas"]).toLocaleString("pt-BR", { minimumFractionDigits: 2 }) }}</td>
                    </tr>
                </tbody> 
            </table>
        </div>
   </section>
</template>

