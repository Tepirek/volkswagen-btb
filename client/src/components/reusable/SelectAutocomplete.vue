<template>
  <v-autocomplete
    chips
    :loading="loading"
    :items="items"
    :label="label"
    :append-icon="icon"
    :rules="rules"
    error-count="1"
    item-value="id"
    :item-text="search"
    clearable
    :value="value"
    @input="$emit('input', $event)"
    return-object
  >
    <template v-slot:selection="data">
      {{ data.item.name }}
    </template>
    <template v-slot:item="data">
      <v-list-item-avatar
        v-if="data.item.marker"
      >
        <v-img :lazy-src="data.item.marker" max-height="24px" max-width="24px"></v-img>
      </v-list-item-avatar>
      <v-list-item-content>
        {{ data.item.name }}
      </v-list-item-content>
    </template>
  </v-autocomplete>
</template>
<script>
export default {
  name: 'SelectAutocomplete',
  props: {
    loading: Boolean,
    items: Array,
    icon: String,
    label: String,
    rules: Array,
    search: String,
    value: Object
  }
}
</script>
