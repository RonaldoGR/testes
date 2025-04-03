


<script>
export default {
    props:{
    msgFooter: {
        type: String,
        required: true
    }
  }
};

</script>


<template>
        <footer>
            <p>{{ msgFooter }}</p>
        </footer>
</template>