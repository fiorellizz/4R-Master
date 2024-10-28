$(document).ready(function() {
    // Botão mobile para abrir/fechar menu
    $('#mobile_btn').on('click', function () {
        $('#mobile_menu').toggleClass('active');
        $('#mobile_btn').find('i').toggleClass('fa-x');
    });

    // Seções e itens do menu de navegação
    const sections = $('section');
    const navItems = $('.nav-item');

    // Evento de rolagem da página
    $(window).on('scroll', function () {
        const header = $('header');
        const scrollPosition = $(window).scrollTop();  // Usando apenas a posição de rolagem

        let activeSectionIndex = 0;

        // Aplicar/remover sombra no header baseado na rolagem
        if (scrollPosition <= 0) {
            header.css('box-shadow', 'none');
        } else {
            header.css('box-shadow', '5px 1px 5px rgba(0, 0, 0, 0.1)'); // Fechamento de parêntese corrigido
        }

        // Identificar qual seção está visível e ajustar a navegação
        sections.each(function(i) {
            const section = $(this);
            const sectionTop = section.offset().top - 96;
            const sectionBottom = sectionTop + section.outerHeight();

            if (scrollPosition >= sectionTop && scrollPosition < sectionBottom) {
                activeSectionIndex = i;
                return false;  // Interrompe o loop quando encontra a seção ativa
            }
        });

        // Atualizar classe 'active' nos itens de navegação
        navItems.removeClass('active');
        $(navItems[activeSectionIndex]).addClass('active');
    });

    // Configuração do ScrollReveal para animações
    ScrollReveal().reveal('#cta', {
        origin: 'left',
        duration: 2000,
        distance: '20%',
        afterReveal: function () {
            console.log("#cta revelado");
        }
    });

    ScrollReveal().reveal('.dish', {
        origin: 'left',
        duration: 2000,
        distance: '20%',
        afterReveal: function () {
            console.log(".dish revelado");
        }
    });

    ScrollReveal().reveal('#testimonial_chef', {
        origin: 'left',
        duration: 1000,
        distance: '20%',
        afterReveal: function () {
            console.log("#testimonial_chef revelado");
        }
    });

    ScrollReveal().reveal('.feedback', {
        origin: 'right',
        duration: 1000,
        distance: '20%',
        afterReveal: function () {
            console.log(".feedback revelado");
        }
    });
});
