<template>
  <Form>
    <p class="h4 text-center mb-4"> Logg inn </p>
    <div class="grey-text">
      <mdb-input label="Email" icon="envelope" type="email"/>
    </div>

    <div>
      <mdb-btn> Login </mdb-btn>
    </div>
  </form>
</template>

<script>
  import {mdbInput, mdbBtn} from 'mdbvue';
  export default {
    name: 'basic',
    components: {
      mdbInput,
      mdbBtn
    },
  }
</script>
