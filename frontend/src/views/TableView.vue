<template>
<div id="app">
  <v-app id="inspire">
    <v-card class="mx-auto mt-10" width="1000" outlined>
      <v-card-title>Contoh Table</v-card-title>
      <v-data-table :headers="headers" :items="parts" :search="search" class="elevation-1" fixed-header height="350px">
        <v-divider inset></v-divider>
        <template v-slot:top>
          <v-toolbar flat color="white">
            <div class="d-flex w-100">
              <v-text-field v-model="search" append-icon="mdi-magnify" label="Search" dense outlined single-line hide-details></v-text-field>
              <v-btn
                color="primary"
                class="ml-2 white--text"
                @click="addNew">
                <v-icon dark>mdi-plus</v-icon>Add
              </v-btn>
            </div>
          </v-toolbar>
        </template>
        <template v-slot:[`item.part`]="{ item }">
          <v-text-field v-model="editedItem.part" :hide-details="true" dense single-line :autofocus="true" v-if="item.id === editedItem.id"></v-text-field>
          <span v-else>{{item.part}}</span>
        </template>
        <template v-slot:[`item.weight`]="{ item }">
          <v-text-field v-model="editedItem.weight" :hide-details="true" dense single-line v-if="item.id === editedItem.id" ></v-text-field>
          <span v-else>{{item.weight}}</span>
        </template>
        <template v-slot:[`item.actions`]="{ item }">
          <div v-if="item.id === editedItem.id">
            <v-icon color="red" class="mr-3" @click="close">
              mdi-window-close
            </v-icon>
            <v-icon color="green"  @click="save">
              mdi-content-save
            </v-icon>
          </div>
          <div v-else>
            <v-icon color="blue" class="mr-3" @click="selectItem(item.part)">
                mdi-check
            </v-icon>
            <v-icon color="green" class="mr-3" @click="editItem(item)">
              mdi-pencil
            </v-icon>
            <v-icon color="red" @click="deleteItem(item)">
              mdi-delete
            </v-icon>
          </div>
        </template>
        <template v-slot:no-data>
          <v-btn color="primary" @click="initialize">Reset</v-btn>
        </template>
      </v-data-table>
    </v-card>
  </v-app>
</div>
</template>

<script>
export default {
    data: () => ({
    search: '',
    headers: [
      {
        text: 'Part',
        value: 'part',
        sortable: false
      },
      {
        text: 'Weight (Kg)',
        value: 'weight',
        sortable: false
      },
      { text: 'Actions', value: 'actions', sortable: false , width: "150px"},
    ],
    parts: [],
    editedIndex: -1,
    editedItem: {
      id: 0,
      part: '',
      weight: 0
    },
    defaultItem: {
      id: 0,
      part: 'New Item',
      weight: 0
    }
  }),
  created () {
    this.initialize();
  },

  methods: {
    initialize () {
      this.parts = [
        {
          id: 1,
          part: 'Bogie',
          weight: 120
        },
        {
          id: 2,
          part: 'Frame',
          weight: 200
        },
        {
          id: 3,
          part: 'Box',
          weight: 128
        },
        {
          id: 4,
          part: 'Monitor',
          weight: 140
        },
        {
          id: 5,
          part: 'Scanner',
          weight: 159
        },
        {
          id: 6,
          part: 'Body',
          weight: 110
        },
        {
          id: 7,
          part: 'Raspi',
          weight: 132
        },
        {
          id: 8,
          part: 'Printer',
          weight: 45
        },
        {
          id: 9,
          part: 'Power Supply',
          weight: 46
        },
        {
          id: 10,
          part: 'RFID',
          weight: 47
        },
        {
          id: 11,
          part: 'Regulator',
          weight: 48
        },
      ]
    },
    
    selectItem (namaItem) {
      confirm(namaItem);
    },

    editItem (item) {
      this.editedIndex = this.parts.indexOf(item);
      this.editedItem = Object.assign({}, item);
    },

    deleteItem (item) {
      const index = this.parts.indexOf(item);
      confirm('Are you sure you want to delete this item?') && this.parts.splice(index, 1);
    },

    close () {
      setTimeout(() => {
        this.editedItem = Object.assign({}, this.defaultItem);
        this.editedIndex = -1;
      }, 300)
    },
    addNew() {
       const addObj = Object.assign({}, this.defaultItem);
       addObj.id = this.parts.length + 1;
       this.parts.unshift(addObj);
       this.editItem(addObj);
    },
    save () {
      if (this.editedIndex > -1) {
        Object.assign(this.parts[this.editedIndex], this.editedItem)
      }
      this.close()
    },
  },
}
</script>