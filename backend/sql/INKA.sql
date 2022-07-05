CREATE TABLE prd_r_proyek(
    id varchar(4) PRIMARY KEY NOT NULL,
    nama varchar(25) NOT NULL,
    tglDibuat date NOT NULL,
    dueDate date NOT NULL
);

CREATE TABLE prd_r_jenisProduk(
    id varchar(4) PRIMARY KEY NOT NULL,
    nama varchar(25) NOT NULL,
    tglDibuat date NOT NULL
);

CREATE TABLE gen_r_liniProduksi(
    id varchar(4) PRIMARY KEY NOT NULL,
    nama integer(25) NOT NULL,
    dibuat date NOT NULL,
    berlaku date NOT NULL
);

CREATE TABLE prd_r_rincianProyek(
    id varchar(7) PRIMARY KEY NOT NULL,
    jumlah int NOT NULL,
    dueDate date NOT NULL,
    jenisProduk varchar(4) NOT NULL,
    proyek varchar(4) NOT NULL,
    FOREIGN KEY (jenisProduk) REFERENCES prd_r_jenisProduk(id),
    FOREIGN KEY (proyek) REFERENCES prd_r_proyek(id)
);

CREATE TABLE prd_d_produk(
    id varchar(9) PRIMARY KEY NOT NULL,
    rincianProyek varchar(7) NOT NULL,
    FOREIGN KEY (rincianProyek) REFERENCES prd_r_rincianProyek(id)
);

CREATE TABLE prd_r_strukturJnsPrd(
    idNodal varchar(7) PRIMARY KEY NOT NULL,
    indukNodal varchar(7) NOT NULL,
    jnsProduk varchar(4) NOT NULL,
    nama varchar(25) NOT NULL,
    jumlah float NOT NULL,
    satuan varchar(10) NOT NULL,
    FOREIGN KEY (indukNodal) REFERENCES prd_r_strukturJnsPrd(idNodal),
    FOREIGN KEY (jnsProduk) REFERENCES prd_r_jenisProduk(id)
);

CREATE TABLE gen_r_stasiunKerja(
    id varchar(4) PRIMARY KEY NOT NULL,
    nama varchar(25) NOT NULL,
    dibuat DATE NOT NULL,
    berlaku DATE NOT NULL,
    liniproduksi varchar(4),
    FOREIGN KEY (liniproduksi) REFERENCES gen_r_liniproduksi(id)
);

CREATE TABLE prd_r_proses(
    id varchar(9) PRIMARY KEY NOT NULL,
    prosesSebelumnya varchar(9) NOT NULL,
    nodalOutput varchar(7) NOT NULL,
    nama varchar(25) NOT NULL,
    durasi float,
    satuanDurasi varchar(10),
    jenisProses varchar(9),
    FOREIGN KEY (prosesSebelumnya) REFERENCES prd_r_proses(id),
    FOREIGN KEY (nodalOutput) REFERENCES prd_r_strukturJnsPrd(idNodal),
    FOREIGN KEY (jenisProses) REFERENCES prd_r_jenisProduk(id)
);

CREATE TABLE gen_r_mampuProses(
    proses varchar(9) NOT NULL,
    stasiunKerja varchar(4) NOT NULL,
    PRIMARY KEY (proses, stasiunKerja),
    FOREIGN KEY (proses) REFERENCES prd_r_proses(id),
    FOREIGN KEY (stasiunKerja) REFERENCES gen_r_stasiunKerja(id)
);

CREATE TABLE prd_d_operasi(
    id varchar(9) PRIMARY KEY NOT NULL,
    rencanaMulai DATE NOT NULL,
    rencanaSelesai DATE NOT NULL,
    mulai DATE NOT NULL,
    selesai DATE NOT NULL,
    proses varchar(9) NOT NULL,
    stasiunKerja varchar(4) NOT NULL,
    produk varchar(9) NOT NULL,
    FOREIGN KEY (proses) REFERENCES prd_r_proses(id),
    FOREIGN KEY (stasiunkerja) REFERENCES gen_r_stasiunKerja(id),
    FOREIGN KEY (produk) REFERENCES prd_d_produk(id)
);

CREATE TABLE mat_r_ToolType(
    codes varchar(9) PRIMARY KEY NOT NULL,
    nama varchar(10) NOT NULL,
    expired DATE NOT NULL
);

CREATE TABLE mat_r_ToolNeed(
    toolTypeCode varchar(12) NOT NULL,
    processCode varchar(3) NOT NULL,
    idNodeOutput varchar(7) NOT NULL,
    PRIMARY KEY (toolTypeCode, processCode, idNodeOutput),
    FOREIGN KEY (toolTypeCode) REFERENCES mat_r_ToolType(codes),
    FOREIGN KEY (processCode) REFERENCES prd_r_proses(id),
    FOREIGN KEY (idNodeOutput) REFERENCES prd_r_proses(nodalOutput)
);

CREATE TABLE prd_r_jenisproses(
    IDJnsProses varchar(9) PRIMARY KEY NOT NULL,
    namaJenisProses varchar(25) NOT NULL
);

CREATE TABLE gen_r_country(
    code varchar(3) PRIMARY KEY NOT NULL,
    nama varchar(30) NOT NULL
);

CREATE TABLE gen_r_city(
    code varchar(3) PRIMARY KEY NOT NULL,
    nama varchar(30) NOT NULL,
    country varchar(3) NOT NULL,
    FOREIGN KEY(country) REFERENCES gen_r_country(code)
);

CREATE TABLE gen_r_customer(
    id varchar(5) PRIMARY KEY NOT NULL,
    nama varchar(30) NOT NULL,
    adress1 varchar(50) NOT NULL,
    adress2 varchar(50) NOT NULL,
    postalcode varchar(5) NOT NULL,
    phone varchar(20) NOT NULL,
    fax varchar(20) NOT NULL,
    email varchar(20) NOT NULL,
    situs varchar(20) NOT NULL,
    pic varchar(20) NOT NULL,
    remark varchar(50) NOT NULL,
    city varchar(3),
    FOREIGN KEY(city) REFERENCES gen_r_city(code)

);

