<script>
import axios from "axios";


export default {
    
  props: {
    msgTri: {
      type: String,
      required: true
    },
  },
  
    data() {
        return {
            tabela_tri_2024: [],
            apiUrl: "http://127.0.0.1:5000/trimestre2024", 
            mostrarDadosTrimestre2024: false
        };
    },

    methods: {
        getDataTrimestre2024() {
            if (this.mostrarDadosTrimestre2024) {
                this.mostrarDadosTrimestre2024 = false;
                this.tabela_tri_2024 = [];
             
                return;
            }
            
            axios.get(this.apiUrl)
                 .then(response => {
                  console.log("DADOS: ", response)
                    this.tabela_tri_2024 = response.data["TRIMESTRE 2024"];
                    this.mostrarDadosTrimestre2024 = true;
                    
                })
                .catch(error => {
                    console.error("Erro ao buscar os dados: ", error);
                });
            } 
   }
}; 
</script>

<template>
  <section class="container">
          <h2 class="text">{{ msgTri  }}</h2>
        <div>
            <button @click="getDataTrimestre2024">Tabela Trimestre 2024</button>
        </div>
       
        <div>
            <table class ="tabela" v-if="tabela_tri_2024.length > 0" border="1">
                <thead class="cabeçalho">
                    <tr>
                        <th>Razão Social</th>
                        <th>Nome Fantasia</th>
                        <th>Despesas</th>
                    </tr>
                </thead>
                <tbody>
                    <tr  v-for="(item, index) in tabela_tri_2024" :key="index" >
                        <td>{{ item["Razao Social"] }}</td>
                        <td>{{ item["Nome Fantasia"] || "Não Informado" }}</td>
                        <td>R$ {{ Number(item["Despesas"]).toLocaleString("pt-BR", { minimumFractionDigits: 2 }) }}</td>
                    </tr>
                </tbody> 
            </table>
        </div>
  </section>
</template>


