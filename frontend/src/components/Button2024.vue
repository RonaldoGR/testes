
<script>
import axios from "axios";


export default {
    
    props: {
    msg2024: {
      type: String,
      required: true
    }
  },
    data() {
        return {
            tabela2024: [],
            apiUrl: "http://127.0.0.1:5000/2024", 
            mostrarDados2024: false
        };
    },

    methods: {
        getData2024() {
            if (this.mostrarDados2024) {
                this.mostrarDados2024 = false;
                this.tabela2024 = [];
                return;
            }
            
            axios.get(this.apiUrl)
                 .then(response => {
                    console.log("DADOS: ", response)
                    this.tabela2024 = response.data["TABELA 2024"];
                    this.mostrarDados2024 = true;
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
        <h2 class="text">{{ msg2024 }}</h2>
        <div>
            <button  @click="getData2024">Tabela 2024</button>
        </div>
       
        <div>
            <table class ="tabela" v-if="tabela2024.length > 0" border="1">
                <thead class="cabeçalho">
                    <tr>
                        <th>Razão Social</th>
                        <th>Nome Fantasia</th>
                        <th>Despesas</th>
                    </tr>
                </thead>
                <tbody>
                    <tr  v-for="(item, index) in tabela2024" :key="index" >
                        <td>{{ item["Razao Social"] }}</td>
                        <td>{{ item["Nome Fantasia"] || "Não Informado" }}</td>
                        <td>R$ {{ Number(item["Despesas"]).toLocaleString("pt-BR", { minimumFractionDigits: 2 }) }}</td>
                    </tr>
                </tbody> 
            </table>
        </div>
    </section>
</template> 
