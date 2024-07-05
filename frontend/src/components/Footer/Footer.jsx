import React from "react";
import './Footer.css'
import paymentMethodsImage from '../../assets/images/formas_pagamento.png'

function Footer(){
    return (
        <footer>
            <div class="footer-columns">
                <div class="footer-column">
                    <h4>Sobre a Loja</h4>
                    <a href="#">Nossa História</a>
                    <a href="#">Missão e Visão</a>
                    <a href="#">Nossas Lojas</a>
                </div>

                <div class="footer-column">
                    <h4>Dúvidas Frequentes</h4>
                    <a href="#">Como Comprar</a>
                    <a href="#">Política de Trocas</a>
                    <a href="#">Formas de Pagamento</a>
                </div>

                <div class="footer-column">
                    <h4>Fale Conosco</h4>
                    <a href="#">Atendimento ao Cliente</a>
                    <a href="#">Trabalhe Conosco</a>
                    <a href="#">Localização</a>
                </div>
                <div class="footer-column">
                    <h4>Formas de Pagamento</h4>
                    <img src={paymentMethodsImage} alt=""></img>
                </div>
            </div>
        </footer>
    )
}

export default Footer