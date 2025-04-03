<script setup>
import Button from './components/Button.vue'
import ButtonTrimestre2024 from './components/ButtonTrimestre2024.vue'
import Button2024 from './components/Button2024.vue'
import Footer from './components/Footer.vue';

</script>

<template>
  <div class="container-title">
    <h1 class="title">Teste VueJS + Python + Flask</h1>
  </div>
    

  <main >
    <Button2024 msg2024="As 10 operadoras ativas com maiores despesas do ano de 2024" />
    <ButtonTrimestre2024 msgTri="As 10 operadoras ativas com maiores despesas no trimestre de 2024" />
    <Button msg2023="As 10 operadoras ativas com maiores despesas no trimestre de 2023" />
  </main>
  <Footer msgFooter="Desenvolvido por Ronaldo Gandra Rocha" />
</template>

