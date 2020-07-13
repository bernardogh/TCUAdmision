/*==============================================================*/
/* DBMS name:      MySQL 5.0                                    */
/* Created on:     26/2/2020 13:40:08                           */
/*==============================================================*/
use AdmisionUCR;

/*==============================================================*/
/* Table: EXAMEN                                                */
/*==============================================================*/
create table EXAMEN
(
   EXM_CODIGO           int not null primary key AUTO_INCREMENT,
   ANHO                 numeric(8,0)
);

/*==============================================================*/
/* Table: EX_CONTIENE_PRE                                       */
/*==============================================================*/
create table EX_CONTIENE_PRE
(
   CODIGO_PREGUNTA      int not null,
   EXM_CODIGO           int not null,
   primary key (CODIGO_PREGUNTA, EXM_CODIGO)
);

/*==============================================================*/
/* Table: INTENTO                                               */
/*==============================================================*/
create table INTENTO
(
   INT_CODIGO           int not null  primary key AUTO_INCREMENT,
   USU_CODIGO_USUARIO   int not null,
   EXM_CODIGO           int not null,
   INT_FECHA            datetime not null,
   INT_DURACION         datetime not null,
   INT_CALIFICACION     decimal not null
);

/*==============================================================*/
/* Table: PREGUNTA                                              */
/*==============================================================*/
create table PREGUNTA
(
   CODIGO_PREGUNTA      int not null primary key AUTO_INCREMENT,
   PREGUNTA_IMAGEN      longtext,
   PREGUNTA_ENLACE      text,
   TEXTO_PREGUNTA       text not null
);

/*==============================================================*/
/* Table: PRES_COMPUESTA_RESP                                   */
/*==============================================================*/
create table PRES_COMPUESTA_RESP
(
   RESP_CODIGO          int not null,
   CODIGO_PREGUNTA      int not null,
   primary key (RESP_CODIGO, CODIGO_PREGUNTA)
);

/*==============================================================*/
/* Table: RESPUESTA                                             */
/*==============================================================*/
create table RESPUESTA
(
   RESP_CODIGO          int not null primary key AUTO_INCREMENT,
   RESP_CORRECTO        bool,
   TEXTO_RESPUESTA      text not null
);

/*==============================================================*/
/* Table: USUARIO                                               */
/*==============================================================*/
create table USUARIO
(
   USU_CODIGO_USUARIO   int not null  primary key AUTO_INCREMENT,
   USU_NOMBRE           varchar(50) not null,
   USU_APELLIDO         varchar(50) not null,
   USU_CORREO           varchar(50) not null,
   USU_CONTRASENHA      varchar(50) not null,
   USU_TIPO             varchar(50) not null
);

alter table EX_CONTIENE_PRE add constraint FK_EX_CONTIENE_PRE foreign key (CODIGO_PREGUNTA)
      references PREGUNTA (CODIGO_PREGUNTA);

alter table EX_CONTIENE_PRE add constraint FK_EX_CONTIENE_PRE2 foreign key (EXM_CODIGO)
      references EXAMEN (EXM_CODIGO);

alter table INTENTO add constraint FK_INT_TIENE_EX foreign key (EXM_CODIGO)
      references EXAMEN (EXM_CODIGO);

alter table INTENTO add constraint FK_USU_REALIZA_INT foreign key (USU_CODIGO_USUARIO)
      references USUARIO (USU_CODIGO_USUARIO);

alter table PRES_COMPUESTA_RESP add constraint FK_PRES_COMPUESTA_RESP foreign key (RESP_CODIGO)
      references RESPUESTA (RESP_CODIGO);

alter table PRES_COMPUESTA_RESP add constraint FK_PRES_COMPUESTA_RESP2 foreign key (CODIGO_PREGUNTA)
      references PREGUNTA (CODIGO_PREGUNTA);