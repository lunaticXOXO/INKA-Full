<template>
  <v-card
    class="mx-auto text-center mt-6"
    color="gray"
    dark
    max-width="1000"
  >
    <v-card-text>
      <v-sheet color="rgba(0, 0, 0, .12)">
        <v-sparkline
          :value="value"
          color="rgba(255, 255, 255, .7)"
          height="100"
          padding="24"
          stroke-linecap="round"
          smooth
        >
          <template v-slot:label="item">
            Rp.{{ item.value }} Juta
          </template>
        </v-sparkline>
      </v-sheet>
    </v-card-text>

    <v-card-text>
      <div class="text-h4 font-weight-thin">
        Jumlah Pendapatan 1 Minggu Terakhir
      </div>
    </v-card-text>

    <v-divider></v-divider>
  </v-card>
</template>

<script>
  export default {
    data: () => ({
      value: [
        2,
        6,
        15,
        20,
        70,
        80,
        97,
      ],
    }),
  }
</script>