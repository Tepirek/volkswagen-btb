<template>
  <v-dialog
    v-model="display"
    elevation="20"
    persistent
  >
    <v-card>
      asd
    </v-card>
            <img
              class="my-auto"
              style="width: 100%; height: 80vh; object-fit: contain; border: 1px solid black"
              src="http://localhost:8000/media/navigation/kasten_inside.jpg"
              alt="navigation" />
  </v-dialog>
</template>
<script>
export default {
  name: 'ComponentNavigation',
  data () {
    return {
      display: true
    }
  }
}
</script>
