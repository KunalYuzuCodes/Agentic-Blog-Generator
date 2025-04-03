<!DOCTYPE html><html lang="en" class="js-focus-visible js" data-js-focus-visible=""><head>
    
      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width,initial-scale=1">
      
        <meta name="description" content="Agent Framework / shim to use Pydantic with LLMs">
      
      
      
        <link rel="canonical" href="https://ai.pydantic.dev/testing/">
      
      
        <link rel="prev" href="../message-history/">
      
      
        <link rel="next" href="../logfire/">
      
      
      <link rel="icon" href="../favicon.ico">
      <meta name="generator" content="mkdocs-1.6.1, mkdocs-material-9.6.5">
    
    
      
        <title>Unit testing - PydanticAI</title>
      
    
    
      <link rel="stylesheet" href="../assets/stylesheets/main.8608ea7d.min.css">
      
        
        <link rel="stylesheet" href="../assets/stylesheets/palette.06af60db.min.css">
      
      


    
    
      
    
    
      
        
        
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin="">
        <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Roboto:300,300i,400,400i,700,700i%7CRoboto+Mono:400,400i,700,700i&amp;display=fallback">
        <style>:root{--md-text-font:"Roboto";--md-code-font:"Roboto Mono"}</style>
      
    
    
      <link rel="stylesheet" href="../assets/_mkdocstrings.css">
    
      <link rel="stylesheet" href="../extra/tweaks.css">
    
    <script>__md_scope=new URL("..",location),__md_hash=e=>[...e].reduce(((e,_)=>(e<<5)-e+_.charCodeAt(0)),0),__md_get=(e,_=localStorage,t=__md_scope)=>JSON.parse(_.getItem(t.pathname+"."+e)),__md_set=(e,_,t=localStorage,a=__md_scope)=>{try{t.setItem(a.pathname+"."+e,JSON.stringify(_))}catch(e){}}</script>
    
      

    
    
      
        <meta property="og:type" content="website">
      
        <meta property="og:title" content="Unit testing - PydanticAI">
      
        <meta property="og:description" content="Agent Framework / shim to use Pydantic with LLMs">
      
        <meta property="og:image" content="https://ai.pydantic.dev/assets/images/social/testing.png">
      
        <meta property="og:image:type" content="image/png">
      
        <meta property="og:image:width" content="1200">
      
        <meta property="og:image:height" content="630">
      
        <meta property="og:url" content="https://ai.pydantic.dev/testing/">
      
        <meta name="twitter:card" content="summary_large_image">
      
        <meta name="twitter:title" content="Unit testing - PydanticAI">
      
        <meta name="twitter:description" content="Agent Framework / shim to use Pydantic with LLMs">
      
        <meta name="twitter:image" content="https://ai.pydantic.dev/assets/images/social/testing.png">
      
    
    
   <link href="../assets/stylesheets/glightbox.min.css" rel="stylesheet"><style>
    html.glightbox-open { overflow: initial; height: 100%; }
    .gslide-title { margin-top: 0px; user-select: text; }
    .gslide-desc { color: #666; user-select: text; }
    .gslide-image img { background: white; }
    .gscrollbar-fixer { padding-right: 15px; }
    .gdesc-inner { font-size: 0.75rem; }
    body[data-md-color-scheme="slate"] .gdesc-inner { background: var(--md-default-bg-color);}
    body[data-md-color-scheme="slate"] .gslide-title { color: var(--md-default-fg-color);}
    body[data-md-color-scheme="slate"] .gslide-desc { color: var(--md-default-fg-color);}</style> <script src="../assets/javascripts/glightbox.min.js"></script><meta name="theme-color" content="#e92063"><meta name="color-scheme" content="light"></head>
  
  
    
    
      
    
    
    
    
    <body dir="ltr" data-md-color-scheme="default" data-md-color-primary="pink" data-md-color-accent="pink" data-md-color-media="(prefers-color-scheme)">
  
    
    <input class="md-toggle" data-md-toggle="drawer" type="checkbox" id="__drawer" autocomplete="off">
    <input class="md-toggle" data-md-toggle="search" type="checkbox" id="__search" autocomplete="off">
    <label class="md-overlay" for="__drawer"></label>
    <div data-md-component="skip">
      
        
        <a href="#unit-testing" class="md-skip">
          Skip to content
        </a>
      
    </div>
    <div data-md-component="announce">
      
    </div>
    
    
      

  

<header class="md-header md-header--shadow" data-md-component="header">
  <nav class="md-header__inner md-grid" aria-label="Header">
    <a href=".." title="PydanticAI" class="md-header__button md-logo" aria-label="PydanticAI" data-md-component="logo">
      
  <img src="../img/logo-white.svg" alt="logo">

    </a>
    <label class="md-header__button md-icon" for="__drawer">
      
      <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M3 6h18v2H3zm0 5h18v2H3zm0 5h18v2H3z"></path></svg>
    </label>
    <div class="md-header__title" data-md-component="header-title">
      <div class="md-header__ellipsis">
        <div class="md-header__topic">
          <span class="md-ellipsis">
            PydanticAI
          </span>
        </div>
        <div class="md-header__topic" data-md-component="header-topic">
          <span class="md-ellipsis">
            
              Unit testing
            
          </span>
        </div>
      </div>
    </div>
    
      
        <form class="md-header__option" data-md-component="palette">
  
    
    
    
    <input class="md-option" data-md-color-media="(prefers-color-scheme)" data-md-color-scheme="default" data-md-color-primary="pink" data-md-color-accent="pink" aria-label="Switch to light mode" type="radio" name="__palette" id="__palette_0">
    
      <label class="md-header__button md-icon" title="Switch to light mode" for="__palette_1">
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M12 2a7 7 0 0 0-7 7c0 2.38 1.19 4.47 3 5.74V17a1 1 0 0 0 1 1h6a1 1 0 0 0 1-1v-2.26c1.81-1.27 3-3.36 3-5.74a7 7 0 0 0-7-7M9 21a1 1 0 0 0 1 1h4a1 1 0 0 0 1-1v-1H9z"></path></svg>
      </label>
    
  
    
    
    
    <input class="md-option" data-md-color-media="(prefers-color-scheme: light)" data-md-color-scheme="default" data-md-color-primary="pink" data-md-color-accent="pink" aria-label="Switch to dark mode" type="radio" name="__palette" id="__palette_1">
    
      <label class="md-header__button md-icon" title="Switch to dark mode" for="__palette_2" hidden="">
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M12 2a7 7 0 0 1 7 7c0 2.38-1.19 4.47-3 5.74V17a1 1 0 0 1-1 1H9a1 1 0 0 1-1-1v-2.26C6.19 13.47 5 11.38 5 9a7 7 0 0 1 7-7M9 21v-1h6v1a1 1 0 0 1-1 1h-4a1 1 0 0 1-1-1m3-17a5 5 0 0 0-5 5c0 2.05 1.23 3.81 3 4.58V16h4v-2.42c1.77-.77 3-2.53 3-4.58a5 5 0 0 0-5-5"></path></svg>
      </label>
    
  
    
    
    
    <input class="md-option" data-md-color-media="(prefers-color-scheme: dark)" data-md-color-scheme="slate" data-md-color-primary="pink" data-md-color-accent="pink" aria-label="Switch to system preference" type="radio" name="__palette" id="__palette_2">
    
      <label class="md-header__button md-icon" title="Switch to system preference" for="__palette_0" hidden="">
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M9 2c3.87 0 7 3.13 7 7 0 2.38-1.19 4.47-3 5.74V17c0 .55-.45 1-1 1H6c-.55 0-1-.45-1-1v-2.26C3.19 13.47 2 11.38 2 9c0-3.87 3.13-7 7-7M6 21v-1h6v1c0 .55-.45 1-1 1H7c-.55 0-1-.45-1-1M9 4C6.24 4 4 6.24 4 9c0 2.05 1.23 3.81 3 4.58V16h4v-2.42c1.77-.77 3-2.53 3-4.58 0-2.76-2.24-5-5-5m10 9h-2l-3.2 9h1.9l.7-2h3.2l.7 2h1.9zm-2.15 5.65L18 15l1.15 3.65z"></path></svg>
      </label>
    
  
</form>
      
    
    
      <script>var palette=__md_get("__palette");if(palette&&palette.color){if("(prefers-color-scheme)"===palette.color.media){var media=matchMedia("(prefers-color-scheme: light)"),input=document.querySelector(media.matches?"[data-md-color-media='(prefers-color-scheme: light)']":"[data-md-color-media='(prefers-color-scheme: dark)']");palette.color.media=input.getAttribute("data-md-color-media"),palette.color.scheme=input.getAttribute("data-md-color-scheme"),palette.color.primary=input.getAttribute("data-md-color-primary"),palette.color.accent=input.getAttribute("data-md-color-accent")}for(var[key,value]of Object.entries(palette.color))document.body.setAttribute("data-md-color-"+key,value)}</script>
    
    
    
      <label class="md-header__button md-icon" for="__search">
        
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M9.5 3A6.5 6.5 0 0 1 16 9.5c0 1.61-.59 3.09-1.56 4.23l.27.27h.79l5 5-1.5 1.5-5-5v-.79l-.27-.27A6.52 6.52 0 0 1 9.5 16 6.5 6.5 0 0 1 3 9.5 6.5 6.5 0 0 1 9.5 3m0 2C7 5 5 7 5 9.5S7 14 9.5 14 14 12 14 9.5 12 5 9.5 5"></path></svg>
      </label>
      <div class="md-search" role="dialog">
  <label class="md-search__overlay" for="__search"></label>
  <div class="md-search__inner" role="search">
    <form class="md-search__form" name="search">
      <input type="text" id="searchbox" class="md-search__input" name="query" aria-label="Search" placeholder="Search" autocapitalize="off" autocorrect="off" autocomplete="off" spellcheck="false" required="">
      <label class="md-search__icon md-icon" for="__search">

        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M9.5 3A6.5 6.5 0 0 1 16 9.5c0 1.61-.59 3.09-1.56 4.23l.27.27h.79l5 5-1.5 1.5-5-5v-.79l-.27-.27A6.516 6.516 0 0 1 9.5 16 6.5 6.5 0 0 1 3 9.5 6.5 6.5 0 0 1 9.5 3m0 2C7 5 5 7 5 9.5S7 14 9.5 14 14 12 14 9.5 12 5 9.5 5Z"></path></svg>

        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M20 11v2H8l5.5 5.5-1.42 1.42L4.16 12l7.92-7.92L13.5 5.5 8 11h12Z"></path></svg>
      </label>
      <nav class="md-search__options" aria-label="Search">

        <button id="searchbox-clear" type="reset" class="md-search__icon md-icon" title="Clear" aria-label="Clear" tabindex="-1">

          <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M19 6.41 17.59 5 12 10.59 6.41 5 5 6.41 10.59 12 5 17.59 6.41 19 12 13.41 17.59 19 19 17.59 13.41 12 19 6.41Z"></path></svg>
        </button>
      </nav>

        <div class="md-search__suggest"></div>

    </form>
    <div class="md-search__output">
      <div class="md-search__scrollwrap" tabindex="0">
        <div class="md-search-result">
          <div class="md-search-result__meta" id="type-to-start-searching">Type to start searching</div>
          <ol class="md-search-result__list" id="hits" role="presentation" hidden=""></ol>
        </div>
      </div>
    </div>
  </div>
</div>
    
    
      <div class="md-header__source">
        <a href="https://github.com/pydantic/pydantic-ai" title="Go to repository" class="md-source" data-md-component="source">
  <div class="md-source__icon md-icon">
    
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512"><!--! Font Awesome Free 6.7.2 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license/free (Icons: CC BY 4.0, Fonts: SIL OFL 1.1, Code: MIT License) Copyright 2024 Fonticons, Inc.--><path d="M439.55 236.05 244 40.45a28.87 28.87 0 0 0-40.81 0l-40.66 40.63 51.52 51.52c27.06-9.14 52.68 16.77 43.39 43.68l49.66 49.66c34.23-11.8 61.18 31 35.47 56.69-26.49 26.49-70.21-2.87-56-37.34L240.22 199v121.85c25.3 12.54 22.26 41.85 9.08 55a34.34 34.34 0 0 1-48.55 0c-17.57-17.6-11.07-46.91 11.25-56v-123c-20.8-8.51-24.6-30.74-18.64-45L142.57 101 8.45 235.14a28.86 28.86 0 0 0 0 40.81l195.61 195.6a28.86 28.86 0 0 0 40.8 0l194.69-194.69a28.86 28.86 0 0 0 0-40.81"></path></svg>
  </div>
  <div class="md-source__repository">
    pydantic/pydantic-ai
  </div>
</a>
      </div>
    
  </nav>
  
</header>
    
    <div class="md-container" data-md-component="container">
      
      
        
          
        
      
      <main class="md-main" data-md-component="main">
        <div class="md-main__inner md-grid">
          
            
              
              <div class="md-sidebar md-sidebar--primary" data-md-component="sidebar" data-md-type="navigation">
                <div class="md-sidebar__scrollwrap">
                  <div class="md-sidebar__inner">
                    



<nav class="md-nav md-nav--primary" aria-label="Navigation" data-md-level="0">
  <label class="md-nav__title" for="__drawer">
    <a href=".." title="PydanticAI" class="md-nav__button md-logo" aria-label="PydanticAI" data-md-component="logo">
      
  <img src="../img/logo-white.svg" alt="logo">

    </a>
    PydanticAI
  </label>
  
    <div class="md-nav__source">
      <a href="https://github.com/pydantic/pydantic-ai" title="Go to repository" class="md-source" data-md-component="source">
  <div class="md-source__icon md-icon">
    
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512"><!--! Font Awesome Free 6.7.2 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license/free (Icons: CC BY 4.0, Fonts: SIL OFL 1.1, Code: MIT License) Copyright 2024 Fonticons, Inc.--><path d="M439.55 236.05 244 40.45a28.87 28.87 0 0 0-40.81 0l-40.66 40.63 51.52 51.52c27.06-9.14 52.68 16.77 43.39 43.68l49.66 49.66c34.23-11.8 61.18 31 35.47 56.69-26.49 26.49-70.21-2.87-56-37.34L240.22 199v121.85c25.3 12.54 22.26 41.85 9.08 55a34.34 34.34 0 0 1-48.55 0c-17.57-17.6-11.07-46.91 11.25-56v-123c-20.8-8.51-24.6-30.74-18.64-45L142.57 101 8.45 235.14a28.86 28.86 0 0 0 0 40.81l195.61 195.6a28.86 28.86 0 0 0 40.8 0l194.69-194.69a28.86 28.86 0 0 0 0-40.81"></path></svg>
  </div>
  <div class="md-source__repository">
    pydantic/pydantic-ai
  </div>
</a>
    </div>
  
  <ul class="md-nav__list">
    
      
      
  
  
  
  
    <li class="md-nav__item">
      <a href=".." class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Introduction
    
  </span>
  

      </a>
    </li>
  

    
      
      
  
  
  
  
    <li class="md-nav__item">
      <a href="../install/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Installation
    
  </span>
  

      </a>
    </li>
  

    
      
      
  
  
  
  
    <li class="md-nav__item">
      <a href="../help/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Getting Help
    
  </span>
  

      </a>
    </li>
  

    
      
      
  
  
  
  
    <li class="md-nav__item">
      <a href="../contributing/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Contributing
    
  </span>
  

      </a>
    </li>
  

    
      
      
  
  
  
  
    <li class="md-nav__item">
      <a href="../troubleshooting/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Troubleshooting
    
  </span>
  

      </a>
    </li>
  

    
      
      
  
  
    
  
  
  
    
    
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
    
    
      
        
        
      
    
    
    <li class="md-nav__item md-nav__item--active md-nav__item--section md-nav__item--nested">
      
        
        
        <input class="md-nav__toggle md-toggle " type="checkbox" id="__nav_6" checked="">
        
          
          <label class="md-nav__link" for="__nav_6" id="__nav_6_label" tabindex="">
            
  
  <span class="md-ellipsis">
    Documentation
    
  </span>
  

            <span class="md-nav__icon md-icon"></span>
          </label>
        
        <nav class="md-nav" data-md-level="1" aria-labelledby="__nav_6_label" aria-expanded="true">
          <label class="md-nav__title" for="__nav_6">
            <span class="md-nav__icon md-icon"></span>
            Documentation
          </label>
          <ul class="md-nav__list">
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../agents/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Agents
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../models/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Models
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../dependencies/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Dependencies
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../tools/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Function Tools
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../common-tools/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Common Tools
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../results/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Results
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../message-history/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Messages and chat history
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
    
  
  
  
    <li class="md-nav__item md-nav__item--active">
      
      <input class="md-nav__toggle md-toggle" type="checkbox" id="__toc">
      
      
        
      
      
        <label class="md-nav__link md-nav__link--active" for="__toc">
          
  
  <span class="md-ellipsis">
    Unit testing
    
  </span>
  

          <span class="md-nav__icon md-icon"></span>
        </label>
      
      <a href="./" class="md-nav__link md-nav__link--active">
        
  
  <span class="md-ellipsis">
    Unit testing
    
  </span>
  

      </a>
      
        

<nav class="md-nav md-nav--secondary" aria-label="Table of contents">
  
  
  
    
  
  
    <label class="md-nav__title" for="__toc">
      <span class="md-nav__icon md-icon"></span>
      Table of contents
    </label>
    <ul class="md-nav__list" data-md-component="toc">
      
        <li class="md-nav__item">
  <a href="#unit-testing-with-testmodel" class="md-nav__link">
    <span class="md-ellipsis">
      Unit testing with TestModel
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#unit-testing-with-functionmodel" class="md-nav__link">
    <span class="md-ellipsis">
      Unit testing with FunctionModel
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#overriding-model-via-pytest-fixtures" class="md-nav__link">
    <span class="md-ellipsis">
      Overriding model via pytest fixtures
    </span>
  </a>
  
</li>
      
    </ul>
  
</nav>
      
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../logfire/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Debugging and Monitoring
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../multi-agent-applications/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Multi-agent Applications
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../graph/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Graphs
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../evals/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Evals
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../input/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Image, Audio &amp; Document Input
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    
    
      
        
          
        
      
        
      
        
      
        
      
    
    
      
    
    
    <li class="md-nav__item md-nav__item--nested">
      
        
        
        <input class="md-nav__toggle md-toggle " type="checkbox" id="__nav_6_14">
        
          
          
          <div class="md-nav__link md-nav__container">
            <a href="../mcp/" class="md-nav__link ">
              
  
  <span class="md-ellipsis">
    MCP
    
  </span>
  

            </a>
            
              
              <label class="md-nav__link " for="__nav_6_14" id="__nav_6_14_label" tabindex="0">
                <span class="md-nav__icon md-icon"></span>
              </label>
            
          </div>
        
        <nav class="md-nav" data-md-level="2" aria-labelledby="__nav_6_14_label" aria-expanded="false">
          <label class="md-nav__title" for="__nav_6_14">
            <span class="md-nav__icon md-icon"></span>
            MCP
          </label>
          <ul class="md-nav__list">
            
              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../mcp/client/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Client
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../mcp/server/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Server
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../mcp/run-python/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    MCP Run Python
    
  </span>
  

      </a>
    </li>
  

              
            
          </ul>
        </nav>
      
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../cli/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Command Line Interface (CLI)
    
  </span>
  

      </a>
    </li>
  

              
            
          </ul>
        </nav>
      
    </li>
  

    
      
      
  
  
  
  
    
    
      
        
          
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
    
    
      
        
        
      
    
    
    <li class="md-nav__item md-nav__item--section md-nav__item--nested">
      
        
        
        <input class="md-nav__toggle md-toggle " type="checkbox" id="__nav_7">
        
          
          
          <div class="md-nav__link md-nav__container">
            <a href="../examples/" class="md-nav__link ">
              
  
  <span class="md-ellipsis">
    Examples
    
  </span>
  

            </a>
            
              
              <label class="md-nav__link " for="__nav_7" id="__nav_7_label" tabindex="">
                <span class="md-nav__icon md-icon"></span>
              </label>
            
          </div>
        
        <nav class="md-nav" data-md-level="1" aria-labelledby="__nav_7_label" aria-expanded="false">
          <label class="md-nav__title" for="__nav_7">
            <span class="md-nav__icon md-icon"></span>
            Examples
          </label>
          <ul class="md-nav__list">
            
              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../examples/pydantic-model/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Pydantic Model
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../examples/weather-agent/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Weather agent
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../examples/bank-support/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Bank support
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../examples/sql-gen/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    SQL Generation
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../examples/flight-booking/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Flight booking
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../examples/rag/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    RAG
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../examples/stream-markdown/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Stream markdown
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../examples/stream-whales/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Stream whales
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../examples/chat-app/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Chat App with FastAPI
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../examples/question-graph/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Question Graph
    
  </span>
  

      </a>
    </li>
  

              
            
          </ul>
        </nav>
      
    </li>
  

    
      
      
  
  
  
  
    
    
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
    
    
      
        
        
      
    
    
    <li class="md-nav__item md-nav__item--section md-nav__item--nested">
      
        
        
        <input class="md-nav__toggle md-toggle " type="checkbox" id="__nav_8">
        
          
          <label class="md-nav__link" for="__nav_8" id="__nav_8_label" tabindex="">
            
  
  <span class="md-ellipsis">
    API Reference
    
  </span>
  

            <span class="md-nav__icon md-icon"></span>
          </label>
        
        <nav class="md-nav" data-md-level="1" aria-labelledby="__nav_8_label" aria-expanded="false">
          <label class="md-nav__title" for="__nav_8">
            <span class="md-nav__icon md-icon"></span>
            API Reference
          </label>
          <ul class="md-nav__list">
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../api/agent/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.agent
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../api/tools/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.tools
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../api/common_tools/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.common_tools
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../api/result/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.result
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../api/messages/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.messages
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../api/exceptions/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.exceptions
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../api/settings/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.settings
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../api/usage/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.usage
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../api/mcp/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.mcp
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../api/format_as_xml/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.format_as_xml
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../api/models/base/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../api/models/openai/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.openai
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../api/models/anthropic/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.anthropic
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../api/models/bedrock/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.bedrock
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../api/models/cohere/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.cohere
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../api/models/gemini/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.gemini
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../api/models/groq/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.groq
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../api/models/instrumented/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.instrumented
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../api/models/mistral/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.mistral
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../api/models/test/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.test
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../api/models/function/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.function
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../api/models/fallback/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.fallback
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../api/models/wrapper/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.wrapper
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../api/providers/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.providers
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../api/pydantic_graph/graph/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_graph
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../api/pydantic_graph/nodes/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_graph.nodes
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../api/pydantic_graph/persistence/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_graph.persistence
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../api/pydantic_graph/mermaid/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_graph.mermaid
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../api/pydantic_graph/exceptions/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_graph.exceptions
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../api/pydantic_evals/dataset/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_evals.dataset
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../api/pydantic_evals/evaluators/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_evals.evaluators
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../api/pydantic_evals/reporting/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_evals.reporting
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../api/pydantic_evals/otel/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_evals.otel
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../api/pydantic_evals/generation/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_evals.generation
    
  </span>
  

      </a>
    </li>
  

              
            
          </ul>
        </nav>
      
    </li>
  

    
  </ul>
</nav>
                  </div>
                </div>
              </div>
            
            
              
              <div class="md-sidebar md-sidebar--secondary" data-md-component="sidebar" data-md-type="toc" style="top: 48px;">
                <div class="md-sidebar__scrollwrap" style="height: 474px;">
                  <div class="md-sidebar__inner">
                    

<nav class="md-nav md-nav--secondary" aria-label="Table of contents">
  
  
  
    
  
  
    <label class="md-nav__title" for="__toc">
      <span class="md-nav__icon md-icon"></span>
      Table of contents
    </label>
    <ul class="md-nav__list" data-md-component="toc">
      
        <li class="md-nav__item">
  <a href="#unit-testing-with-testmodel" class="md-nav__link">
    <span class="md-ellipsis">
      Unit testing with TestModel
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#unit-testing-with-functionmodel" class="md-nav__link">
    <span class="md-ellipsis">
      Unit testing with FunctionModel
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#overriding-model-via-pytest-fixtures" class="md-nav__link">
    <span class="md-ellipsis">
      Overriding model via pytest fixtures
    </span>
  </a>
  
</li>
      
    </ul>
  
</nav>
                  </div>
                </div>
              </div>
            
          
          
            <div class="md-content" data-md-component="content">
              <article class="md-content__inner md-typeset">
                
                  


  
  


<h1 id="unit-testing">Unit testing</h1>
<p>Writing unit tests for PydanticAI code is just like unit tests for any other Python code.</p>
<p>Because for the most part they're nothing new, we have pretty well established tools and patterns for writing and running these kinds of tests.</p>
<p>Unless you're really sure you know better, you'll probably want to follow roughly this strategy:</p>
<ul>
<li>Use <a href="https://docs.pytest.org/en/stable/"><code>pytest</code></a> as your test harness</li>
<li>If you find yourself typing out long assertions, use <a href="https://15r10nk.github.io/inline-snapshot/latest/">inline-snapshot</a></li>
<li>Similarly, <a href="https://dirty-equals.helpmanual.io/latest/">dirty-equals</a> can be useful for comparing large data structures</li>
<li>Use <a class="autorefs autorefs-internal" href="../api/models/test/#pydantic_ai.models.test.TestModel"><code>TestModel</code></a> or <a class="autorefs autorefs-internal" href="../api/models/function/#pydantic_ai.models.function.FunctionModel"><code>FunctionModel</code></a> in place of your actual model to avoid the usage, latency and variability of real LLM calls</li>
<li>Use <a class="autorefs autorefs-internal" href="../api/agent/#pydantic_ai.agent.Agent.override"><code>Agent.override</code></a> to replace your model inside your application logic</li>
<li>Set <a class="autorefs autorefs-internal" href="../api/models/base/#pydantic_ai.models.ALLOW_MODEL_REQUESTS"><code>ALLOW_MODEL_REQUESTS=False</code></a> globally to block any requests from being made to non-test models accidentally</li>
</ul>
<h3 id="unit-testing-with-testmodel">Unit testing with <code>TestModel</code></h3>
<p>The simplest and fastest way to exercise most of your application code is using <a class="autorefs autorefs-internal" href="../api/models/test/#pydantic_ai.models.test.TestModel"><code>TestModel</code></a>, this will (by default) call all tools in the agent, then return either plain text or a structured response depending on the return type of the agent.</p>
<div class="admonition note">
<p class="admonition-title"><code>TestModel</code> is not magic</p>
<p>The "clever" (but not too clever) part of <code>TestModel</code> is that it will attempt to generate valid structured data for <a href="../tools/">function tools</a> and <a href="../results/#structured-result-validation">result types</a> based on the schema of the registered tools.</p>
<p>There's no ML or AI in <code>TestModel</code>, it's just plain old procedural Python code that tries to generate data that satisfies the JSON schema of a tool.</p>
<p>The resulting data won't look pretty or relevant, but it should pass Pydantic's validation in most cases.
If you want something more sophisticated, use <a class="autorefs autorefs-internal" href="../api/models/function/#pydantic_ai.models.function.FunctionModel"><code>FunctionModel</code></a> and write your own data generation logic.</p>
</div>
<p>Let's write unit tests for the following application code:</p>
<div class="language-python highlight"><span class="filename">weather_app.py</span><pre id="__code_0"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_0 > code"></button><code><span class="kn">import</span><span class="w"> </span><span class="nn">asyncio</span>
<span class="kn">from</span><span class="w"> </span><span class="nn">datetime</span><span class="w"> </span><span class="kn">import</span> <span class="n">date</span>

<span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_ai</span><span class="w"> </span><span class="kn">import</span> <span class="n">Agent</span><span class="p">,</span> <span class="n">RunContext</span>

<span class="kn">from</span><span class="w"> </span><span class="nn">fake_database</span><span class="w"> </span><span class="kn">import</span> <span class="n">DatabaseConn</span>  <span class="c1"><aside class="md-annotation" tabindex="0" style="--md-tooltip-x: 354px; --md-tooltip-y: 115px; --md-tooltip-0: -16px;"><div class="md-tooltip" id="__code_0_annotation_1" role="tooltip"><div class="md-tooltip__inner md-typeset"><code>DatabaseConn</code> is a class that holds a database connection</div></div><a href="#__code_0_annotation_1" class="md-annotation__index" tabindex="-1"><span data-md-annotation-id="1"></span></a></aside></span>
<span class="kn">from</span><span class="w"> </span><span class="nn">weather_service</span><span class="w"> </span><span class="kn">import</span> <span class="n">WeatherService</span>  <span class="c1"><aside class="md-annotation" tabindex="0" style="--md-tooltip-x: 387px; --md-tooltip-y: 134px; --md-tooltip-0: -16px;"><div class="md-tooltip" id="__code_0_annotation_2" role="tooltip"><div class="md-tooltip__inner md-typeset"><code>WeatherService</code> has methods to get weather forecasts and historic data about the weather</div></div><a href="#__code_0_annotation_2" class="md-annotation__index" tabindex="-1"><span data-md-annotation-id="2"></span></a></aside></span>

<span class="n">weather_agent</span> <span class="o">=</span> <span class="n">Agent</span><span class="p">(</span>
    <span class="s1">'openai:gpt-4o'</span><span class="p">,</span>
    <span class="n">deps_type</span><span class="o">=</span><span class="n">WeatherService</span><span class="p">,</span>
    <span class="n">system_prompt</span><span class="o">=</span><span class="s1">'Providing a weather forecast at the locations the user provides.'</span><span class="p">,</span>
<span class="p">)</span>


<span class="nd">@weather_agent</span><span class="o">.</span><span class="n">tool</span>
<span class="k">def</span><span class="w"> </span><span class="nf">weather_forecast</span><span class="p">(</span>
    <span class="n">ctx</span><span class="p">:</span> <span class="n">RunContext</span><span class="p">[</span><span class="n">WeatherService</span><span class="p">],</span> <span class="n">location</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">forecast_date</span><span class="p">:</span> <span class="n">date</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
    <span class="k">if</span> <span class="n">forecast_date</span> <span class="o">&lt;</span> <span class="n">date</span><span class="o">.</span><span class="n">today</span><span class="p">():</span>  <span class="c1"><aside class="md-annotation" tabindex="0" style="--md-tooltip-x: 338px; --md-tooltip-y: 382px; --md-tooltip-0: -16px;"><div class="md-tooltip" id="__code_0_annotation_3" role="tooltip"><div class="md-tooltip__inner md-typeset">We need to call a different endpoint depending on whether the date is in the past or the future, you'll see why this nuance is important below</div></div><a href="#__code_0_annotation_3" class="md-annotation__index" tabindex="-1"><span data-md-annotation-id="3"></span></a></aside></span>
        <span class="k">return</span> <span class="n">ctx</span><span class="o">.</span><span class="n">deps</span><span class="o">.</span><span class="n">get_historic_weather</span><span class="p">(</span><span class="n">location</span><span class="p">,</span> <span class="n">forecast_date</span><span class="p">)</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="k">return</span> <span class="n">ctx</span><span class="o">.</span><span class="n">deps</span><span class="o">.</span><span class="n">get_forecast</span><span class="p">(</span><span class="n">location</span><span class="p">,</span> <span class="n">forecast_date</span><span class="p">)</span>


<span class="k">async</span> <span class="k">def</span><span class="w"> </span><span class="nf">run_weather_forecast</span><span class="p">(</span>  <span class="c1"><aside class="md-annotation" tabindex="0" style="--md-tooltip-x: 297px; --md-tooltip-y: 496px; --md-tooltip-0: -16px;"><div class="md-tooltip" id="__code_0_annotation_4" role="tooltip"><div class="md-tooltip__inner md-typeset">This function is the code we want to test, together with the agent it uses</div></div><a href="#__code_0_annotation_4" class="md-annotation__index" tabindex="-1"><span data-md-annotation-id="4"></span></a></aside></span>
    <span class="n">user_prompts</span><span class="p">:</span> <span class="nb">list</span><span class="p">[</span><span class="nb">tuple</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">int</span><span class="p">]],</span> <span class="n">conn</span><span class="p">:</span> <span class="n">DatabaseConn</span>
<span class="p">):</span>
<span class="w">    </span><span class="sd">"""Run weather forecast for a list of user prompts and save."""</span>
    <span class="k">async</span> <span class="k">with</span> <span class="n">WeatherService</span><span class="p">()</span> <span class="k">as</span> <span class="n">weather_service</span><span class="p">:</span>

        <span class="k">async</span> <span class="k">def</span><span class="w"> </span><span class="nf">run_forecast</span><span class="p">(</span><span class="n">prompt</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">user_id</span><span class="p">:</span> <span class="nb">int</span><span class="p">):</span>
            <span class="n">result</span> <span class="o">=</span> <span class="k">await</span> <span class="n">weather_agent</span><span class="o">.</span><span class="n">run</span><span class="p">(</span><span class="n">prompt</span><span class="p">,</span> <span class="n">deps</span><span class="o">=</span><span class="n">weather_service</span><span class="p">)</span>
            <span class="k">await</span> <span class="n">conn</span><span class="o">.</span><span class="n">store_forecast</span><span class="p">(</span><span class="n">user_id</span><span class="p">,</span> <span class="n">result</span><span class="o">.</span><span class="n">data</span><span class="p">)</span>

        <span class="c1"># run all prompts in parallel</span>
        <span class="k">await</span> <span class="n">asyncio</span><span class="o">.</span><span class="n">gather</span><span class="p">(</span>
            <span class="o">*</span><span class="p">(</span><span class="n">run_forecast</span><span class="p">(</span><span class="n">prompt</span><span class="p">,</span> <span class="n">user_id</span><span class="p">)</span> <span class="k">for</span> <span class="p">(</span><span class="n">prompt</span><span class="p">,</span> <span class="n">user_id</span><span class="p">)</span> <span class="ow">in</span> <span class="n">user_prompts</span><span class="p">)</span>
        <span class="p">)</span>
</code></pre></div>
<ol hidden="">
<li></li>
<li></li>
<li></li>
<li></li>
</ol>
<p>Here we have a function that takes a list of <code class="language-python highlight"><span class="p">(</span><span class="n">user_prompt</span><span class="p">,</span> <span class="n">user_id</span><span class="p">)</span></code> tuples, gets a weather forecast for each prompt, and stores the result in the database.</p>
<p><strong>We want to test this code without having to mock certain objects or modify our code so we can pass test objects in.</strong></p>
<p>Here's how we would write tests using <a class="autorefs autorefs-internal" href="../api/models/test/#pydantic_ai.models.test.TestModel"><code>TestModel</code></a>:</p>
<div class="language-python highlight"><span class="filename">test_weather_app.py</span><pre id="__code_1"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_1 > code"></button><code tabindex="0"><span class="kn">from</span><span class="w"> </span><span class="nn">datetime</span><span class="w"> </span><span class="kn">import</span> <span class="n">timezone</span>
<span class="kn">import</span><span class="w"> </span><span class="nn">pytest</span>

<span class="kn">from</span><span class="w"> </span><span class="nn">dirty_equals</span><span class="w"> </span><span class="kn">import</span> <span class="n">IsNow</span><span class="p">,</span> <span class="n">IsStr</span>

<span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_ai</span><span class="w"> </span><span class="kn">import</span> <span class="n">models</span><span class="p">,</span> <span class="n">capture_run_messages</span>
<span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_ai.models.test</span><span class="w"> </span><span class="kn">import</span> <span class="n">TestModel</span>
<span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_ai.messages</span><span class="w"> </span><span class="kn">import</span> <span class="p">(</span>
    <span class="n">ModelResponse</span><span class="p">,</span>
    <span class="n">SystemPromptPart</span><span class="p">,</span>
    <span class="n">TextPart</span><span class="p">,</span>
    <span class="n">ToolCallPart</span><span class="p">,</span>
    <span class="n">ToolReturnPart</span><span class="p">,</span>
    <span class="n">UserPromptPart</span><span class="p">,</span>
    <span class="n">ModelRequest</span><span class="p">,</span>
<span class="p">)</span>

<span class="kn">from</span><span class="w"> </span><span class="nn">fake_database</span><span class="w"> </span><span class="kn">import</span> <span class="n">DatabaseConn</span>
<span class="kn">from</span><span class="w"> </span><span class="nn">weather_app</span><span class="w"> </span><span class="kn">import</span> <span class="n">run_weather_forecast</span><span class="p">,</span> <span class="n">weather_agent</span>

<span class="n">pytestmark</span> <span class="o">=</span> <span class="n">pytest</span><span class="o">.</span><span class="n">mark</span><span class="o">.</span><span class="n">anyio</span>  <span class="c1"><aside class="md-annotation" tabindex="0" style="--md-tooltip-x: 289px; --md-tooltip-y: 401px; --md-tooltip-0: -16px;"><div class="md-tooltip" id="__code_1_annotation_1" role="tooltip"><div class="md-tooltip__inner md-typeset">We're using <a href="https://anyio.readthedocs.io/en/stable/">anyio</a> to run async tests.</div></div><a href="#__code_1_annotation_1" class="md-annotation__index" tabindex="-1"><span data-md-annotation-id="1"></span></a></aside></span>
<span class="n">models</span><span class="o">.</span><span class="n">ALLOW_MODEL_REQUESTS</span> <span class="o">=</span> <span class="kc">False</span>  <span class="c1"><aside class="md-annotation" tabindex="0" style="--md-tooltip-x: 330px; --md-tooltip-y: 420px; --md-tooltip-0: -16px;"><div class="md-tooltip" id="__code_1_annotation_2" role="tooltip"><div class="md-tooltip__inner md-typeset">This is a safety measure to make sure we don't accidentally make real requests to the LLM while testing, see <a class="autorefs autorefs-internal" href="../api/models/base/#pydantic_ai.models.ALLOW_MODEL_REQUESTS"><code>ALLOW_MODEL_REQUESTS</code></a> for more details.</div></div><a href="#__code_1_annotation_2" class="md-annotation__index" tabindex="-1"><span data-md-annotation-id="2"></span></a></aside></span>


<span class="k">async</span> <span class="k">def</span><span class="w"> </span><span class="nf">test_forecast</span><span class="p">():</span>
    <span class="n">conn</span> <span class="o">=</span> <span class="n">DatabaseConn</span><span class="p">()</span>
    <span class="n">user_id</span> <span class="o">=</span> <span class="mi">1</span>
    <span class="k">with</span> <span class="n">capture_run_messages</span><span class="p">()</span> <span class="k">as</span> <span class="n">messages</span><span class="p">:</span>
        <span class="k">with</span> <span class="n">weather_agent</span><span class="o">.</span><span class="n">override</span><span class="p">(</span><span class="n">model</span><span class="o">=</span><span class="n">TestModel</span><span class="p">()):</span>  <span class="c1"><aside class="md-annotation" tabindex="0" style="--md-tooltip-x: 493px; --md-tooltip-y: 553px; --md-tooltip-0: -16px;"><div class="md-tooltip" id="__code_1_annotation_3" role="tooltip"><div class="md-tooltip__inner md-typeset">We're using <a class="autorefs autorefs-internal" href="../api/agent/#pydantic_ai.agent.Agent.override"><code>Agent.override</code></a> to replace the agent's model with <a class="autorefs autorefs-internal" href="../api/models/test/#pydantic_ai.models.test.TestModel"><code>TestModel</code></a>, the nice thing about <code>override</code> is that we can replace the model inside agent without needing access to the agent <code>run*</code> methods call site.</div></div><a href="#__code_1_annotation_3" class="md-annotation__index" tabindex="-1"><span data-md-annotation-id="3"></span></a></aside></span>
            <span class="n">prompt</span> <span class="o">=</span> <span class="s1">'What will the weather be like in London on 2024-11-28?'</span>
            <span class="k">await</span> <span class="n">run_weather_forecast</span><span class="p">([(</span><span class="n">prompt</span><span class="p">,</span> <span class="n">user_id</span><span class="p">)],</span> <span class="n">conn</span><span class="p">)</span>  <span class="c1"><aside class="md-annotation" tabindex="0" style="--md-tooltip-x: 575px; --md-tooltip-y: 591px; --md-tooltip-0: -16px;"><div class="md-tooltip" id="__code_1_annotation_4" role="tooltip"><div class="md-tooltip__inner md-typeset">Now we call the function we want to test inside the <code>override</code> context manager.</div></div><a href="#__code_1_annotation_4" class="md-annotation__index" tabindex="-1"><span data-md-annotation-id="4"></span></a></aside></span>

    <span class="n">forecast</span> <span class="o">=</span> <span class="k">await</span> <span class="n">conn</span><span class="o">.</span><span class="n">get_forecast</span><span class="p">(</span><span class="n">user_id</span><span class="p">)</span>
    <span class="k">assert</span> <span class="n">forecast</span> <span class="o">==</span> <span class="s1">'{"weather_forecast":"Sunny with a chance of rain"}'</span>  <span class="c1"><aside class="md-annotation" tabindex="0" style="--md-tooltip-x: 656px; --md-tooltip-y: 648px; --md-tooltip-0: -16px;"><div class="md-tooltip" id="__code_1_annotation_5" role="tooltip"><div class="md-tooltip__inner md-typeset">But default, <code>TestModel</code> will return a JSON string summarising the tools calls made, and what was returned. If you wanted to customise the response to something more closely aligned with the domain, you could add <a class="autorefs autorefs-internal" href="../api/models/test/#pydantic_ai.models.test.TestModel.custom_result_text"><code>custom_result_text='Sunny'</code></a> when defining <code>TestModel</code>.</div></div><a href="#__code_1_annotation_5" class="md-annotation__index" tabindex="-1"><span data-md-annotation-id="5"></span></a></aside></span>

    <span class="k">assert</span> <span class="n">messages</span> <span class="o">==</span> <span class="p">[</span>  <span class="c1"><aside class="md-annotation" tabindex="0" style="--md-tooltip-x: 240px; --md-tooltip-y: 686px; --md-tooltip-0: -16px;"><div class="md-tooltip" id="__code_1_annotation_6" role="tooltip"><div class="md-tooltip__inner md-typeset">So far we don't actually know which tools were called and with which values, we can use <a class="autorefs autorefs-internal" href="../api/agent/#pydantic_ai.agent.capture_run_messages"><code>capture_run_messages</code></a> to inspect messages from the most recent run and assert the exchange between the agent and the model occurred as expected.</div></div><a href="#__code_1_annotation_6" class="md-annotation__index" tabindex="-1"><span data-md-annotation-id="6"></span></a></aside></span>
        <span class="n">ModelRequest</span><span class="p">(</span>
            <span class="n">parts</span><span class="o">=</span><span class="p">[</span>
                <span class="n">SystemPromptPart</span><span class="p">(</span>
                    <span class="n">content</span><span class="o">=</span><span class="s1">'Providing a weather forecast at the locations the user provides.'</span><span class="p">,</span>
                    <span class="n">timestamp</span><span class="o">=</span><span class="n">IsNow</span><span class="p">(</span><span class="n">tz</span><span class="o">=</span><span class="n">timezone</span><span class="o">.</span><span class="n">utc</span><span class="p">),</span>
                <span class="p">),</span>
                <span class="n">UserPromptPart</span><span class="p">(</span>
                    <span class="n">content</span><span class="o">=</span><span class="s1">'What will the weather be like in London on 2024-11-28?'</span><span class="p">,</span>
                    <span class="n">timestamp</span><span class="o">=</span><span class="n">IsNow</span><span class="p">(</span><span class="n">tz</span><span class="o">=</span><span class="n">timezone</span><span class="o">.</span><span class="n">utc</span><span class="p">),</span>  <span class="c1"><aside class="md-annotation" tabindex="0" style="--md-tooltip-x: 477px; --md-tooltip-y: 858px; --md-tooltip-0: -16px;"><div class="md-tooltip" id="__code_1_annotation_7" role="tooltip"><div class="md-tooltip__inner md-typeset">The <a class="autorefs autorefs-external" href="https://dirty-equals.helpmanual.io/latest/types/datetime/#dirty_equals.IsNow"><code>IsNow</code></a> helper allows us to use declarative asserts even with data which will contain timestamps that change over time.</div></div><a href="#__code_1_annotation_7" class="md-annotation__index" tabindex="-1"><span data-md-annotation-id="7"></span></a></aside></span>
                <span class="p">),</span>
            <span class="p">]</span>
        <span class="p">),</span>
        <span class="n">ModelResponse</span><span class="p">(</span>
            <span class="n">parts</span><span class="o">=</span><span class="p">[</span>
                <span class="n">ToolCallPart</span><span class="p">(</span>
                    <span class="n">tool_name</span><span class="o">=</span><span class="s1">'weather_forecast'</span><span class="p">,</span>
                    <span class="n">args</span><span class="o">=</span><span class="p">{</span>
                        <span class="s1">'location'</span><span class="p">:</span> <span class="s1">'a'</span><span class="p">,</span>
                        <span class="s1">'forecast_date'</span><span class="p">:</span> <span class="s1">'2024-01-01'</span><span class="p">,</span>  <span class="c1"><aside class="md-annotation" tabindex="0" style="--md-tooltip-x: 485px; --md-tooltip-y: 1048px; --md-tooltip-0: -16px;"><div class="md-tooltip" id="__code_1_annotation_8" role="tooltip"><div class="md-tooltip__inner md-typeset"><code>TestModel</code> isn't doing anything clever to extract values from the prompt, so these values are hardcoded.</div></div><a href="#__code_1_annotation_8" class="md-annotation__index" tabindex="-1"><span data-md-annotation-id="8"></span></a></aside></span>
                    <span class="p">},</span>
                    <span class="n">tool_call_id</span><span class="o">=</span><span class="n">IsStr</span><span class="p">(),</span>
                <span class="p">)</span>
            <span class="p">],</span>
            <span class="n">model_name</span><span class="o">=</span><span class="s1">'test'</span><span class="p">,</span>
            <span class="n">timestamp</span><span class="o">=</span><span class="n">IsNow</span><span class="p">(</span><span class="n">tz</span><span class="o">=</span><span class="n">timezone</span><span class="o">.</span><span class="n">utc</span><span class="p">),</span>
        <span class="p">),</span>
        <span class="n">ModelRequest</span><span class="p">(</span>
            <span class="n">parts</span><span class="o">=</span><span class="p">[</span>
                <span class="n">ToolReturnPart</span><span class="p">(</span>
                    <span class="n">tool_name</span><span class="o">=</span><span class="s1">'weather_forecast'</span><span class="p">,</span>
                    <span class="n">content</span><span class="o">=</span><span class="s1">'Sunny with a chance of rain'</span><span class="p">,</span>
                    <span class="n">tool_call_id</span><span class="o">=</span><span class="n">IsStr</span><span class="p">(),</span>
                    <span class="n">timestamp</span><span class="o">=</span><span class="n">IsNow</span><span class="p">(</span><span class="n">tz</span><span class="o">=</span><span class="n">timezone</span><span class="o">.</span><span class="n">utc</span><span class="p">),</span>
                <span class="p">),</span>
            <span class="p">],</span>
        <span class="p">),</span>
        <span class="n">ModelResponse</span><span class="p">(</span>
            <span class="n">parts</span><span class="o">=</span><span class="p">[</span>
                <span class="n">TextPart</span><span class="p">(</span>
                    <span class="n">content</span><span class="o">=</span><span class="s1">'{"weather_forecast":"Sunny with a chance of rain"}'</span><span class="p">,</span>
                <span class="p">)</span>
            <span class="p">],</span>
            <span class="n">model_name</span><span class="o">=</span><span class="s1">'test'</span><span class="p">,</span>
            <span class="n">timestamp</span><span class="o">=</span><span class="n">IsNow</span><span class="p">(</span><span class="n">tz</span><span class="o">=</span><span class="n">timezone</span><span class="o">.</span><span class="n">utc</span><span class="p">),</span>
        <span class="p">),</span>
    <span class="p">]</span>
</code></pre></div>
<ol hidden="">
<li></li>
<li></li>
<li></li>
<li></li>
<li></li>
<li></li>
<li></li>
<li></li>
</ol>
<h3 id="unit-testing-with-functionmodel">Unit testing with <code>FunctionModel</code></h3>
<p>The above tests are a great start, but careful readers will notice that the <code>WeatherService.get_forecast</code> is never called since <code>TestModel</code> calls <code>weather_forecast</code> with a date in the past.</p>
<p>To fully exercise <code>weather_forecast</code>, we need to use <a class="autorefs autorefs-internal" href="../api/models/function/#pydantic_ai.models.function.FunctionModel"><code>FunctionModel</code></a> to customise how the tools is called.</p>
<p>Here's an example of using <code>FunctionModel</code> to test the <code>weather_forecast</code> tool with custom inputs</p>
<div class="language-python highlight"><span class="filename">test_weather_app2.py</span><pre id="__code_2"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_2 > code"></button><code><span class="kn">import</span><span class="w"> </span><span class="nn">re</span>

<span class="kn">import</span><span class="w"> </span><span class="nn">pytest</span>

<span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_ai</span><span class="w"> </span><span class="kn">import</span> <span class="n">models</span>
<span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_ai.messages</span><span class="w"> </span><span class="kn">import</span> <span class="p">(</span>
    <span class="n">ModelMessage</span><span class="p">,</span>
    <span class="n">ModelResponse</span><span class="p">,</span>
    <span class="n">TextPart</span><span class="p">,</span>
    <span class="n">ToolCallPart</span><span class="p">,</span>
<span class="p">)</span>
<span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_ai.models.function</span><span class="w"> </span><span class="kn">import</span> <span class="n">AgentInfo</span><span class="p">,</span> <span class="n">FunctionModel</span>

<span class="kn">from</span><span class="w"> </span><span class="nn">fake_database</span><span class="w"> </span><span class="kn">import</span> <span class="n">DatabaseConn</span>
<span class="kn">from</span><span class="w"> </span><span class="nn">weather_app</span><span class="w"> </span><span class="kn">import</span> <span class="n">run_weather_forecast</span><span class="p">,</span> <span class="n">weather_agent</span>

<span class="n">pytestmark</span> <span class="o">=</span> <span class="n">pytest</span><span class="o">.</span><span class="n">mark</span><span class="o">.</span><span class="n">anyio</span>
<span class="n">models</span><span class="o">.</span><span class="n">ALLOW_MODEL_REQUESTS</span> <span class="o">=</span> <span class="kc">False</span>


<span class="k">def</span><span class="w"> </span><span class="nf">call_weather_forecast</span><span class="p">(</span>  <span class="c1"><aside class="md-annotation" tabindex="0" style="--md-tooltip-x: 257px; --md-tooltip-y: 401px; --md-tooltip-0: -16px;"><div class="md-tooltip" id="__code_2_annotation_1" role="tooltip"><div class="md-tooltip__inner md-typeset">We define a function <code>call_weather_forecast</code> that will be called by <code>FunctionModel</code> in place of the LLM, this function has access to the list of <a class="autorefs autorefs-internal" href="../api/messages/#pydantic_ai.messages.ModelMessage"><code>ModelMessage</code></a>s that make up the run, and <a class="autorefs autorefs-internal" href="../api/models/function/#pydantic_ai.models.function.AgentInfo"><code>AgentInfo</code></a> which contains information about the agent and the function tools and return tools.</div></div><a href="#__code_2_annotation_1" class="md-annotation__index" tabindex="-1"><span data-md-annotation-id="1"></span></a></aside></span>
    <span class="n">messages</span><span class="p">:</span> <span class="nb">list</span><span class="p">[</span><span class="n">ModelMessage</span><span class="p">],</span> <span class="n">info</span><span class="p">:</span> <span class="n">AgentInfo</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ModelResponse</span><span class="p">:</span>
    <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">messages</span><span class="p">)</span> <span class="o">==</span> <span class="mi">1</span><span class="p">:</span>
        <span class="c1"># first call, call the weather forecast tool</span>
        <span class="n">user_prompt</span> <span class="o">=</span> <span class="n">messages</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">parts</span><span class="p">[</span><span class="o">-</span><span class="mi">1</span><span class="p">]</span>
        <span class="n">m</span> <span class="o">=</span> <span class="n">re</span><span class="o">.</span><span class="n">search</span><span class="p">(</span><span class="sa">r</span><span class="s1">'\d</span><span class="si">{4}</span><span class="s1">-\d</span><span class="si">{2}</span><span class="s1">-\d</span><span class="si">{2}</span><span class="s1">'</span><span class="p">,</span> <span class="n">user_prompt</span><span class="o">.</span><span class="n">content</span><span class="p">)</span>
        <span class="k">assert</span> <span class="n">m</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span>
        <span class="n">args</span> <span class="o">=</span> <span class="p">{</span><span class="s1">'location'</span><span class="p">:</span> <span class="s1">'London'</span><span class="p">,</span> <span class="s1">'forecast_date'</span><span class="p">:</span> <span class="n">m</span><span class="o">.</span><span class="n">group</span><span class="p">()}</span>  <span class="c1"><aside class="md-annotation" tabindex="0" style="--md-tooltip-x: 575px; --md-tooltip-y: 553px; --md-tooltip-0: -16px;"><div class="md-tooltip" id="__code_2_annotation_2" role="tooltip"><div class="md-tooltip__inner md-typeset">Our function is slightly intelligent in that it tries to extract a date from the prompt, but just hard codes the location.</div></div><a href="#__code_2_annotation_2" class="md-annotation__index" tabindex="-1"><span data-md-annotation-id="2"></span></a></aside></span>
        <span class="k">return</span> <span class="n">ModelResponse</span><span class="p">(</span><span class="n">parts</span><span class="o">=</span><span class="p">[</span><span class="n">ToolCallPart</span><span class="p">(</span><span class="s1">'weather_forecast'</span><span class="p">,</span> <span class="n">args</span><span class="p">)])</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="c1"># second call, return the forecast</span>
        <span class="n">msg</span> <span class="o">=</span> <span class="n">messages</span><span class="p">[</span><span class="o">-</span><span class="mi">1</span><span class="p">]</span><span class="o">.</span><span class="n">parts</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span>
        <span class="k">assert</span> <span class="n">msg</span><span class="o">.</span><span class="n">part_kind</span> <span class="o">==</span> <span class="s1">'tool-return'</span>
        <span class="k">return</span> <span class="n">ModelResponse</span><span class="p">(</span><span class="n">parts</span><span class="o">=</span><span class="p">[</span><span class="n">TextPart</span><span class="p">(</span><span class="sa">f</span><span class="s1">'The forecast is: </span><span class="si">{</span><span class="n">msg</span><span class="o">.</span><span class="n">content</span><span class="si">}</span><span class="s1">'</span><span class="p">)])</span>


<span class="k">async</span> <span class="k">def</span><span class="w"> </span><span class="nf">test_forecast_future</span><span class="p">():</span>
    <span class="n">conn</span> <span class="o">=</span> <span class="n">DatabaseConn</span><span class="p">()</span>
    <span class="n">user_id</span> <span class="o">=</span> <span class="mi">1</span>
    <span class="k">with</span> <span class="n">weather_agent</span><span class="o">.</span><span class="n">override</span><span class="p">(</span><span class="n">model</span><span class="o">=</span><span class="n">FunctionModel</span><span class="p">(</span><span class="n">call_weather_forecast</span><span class="p">)):</span>  <span class="c1"><aside class="md-annotation" tabindex="0" style="--md-tooltip-x: 665px; --md-tooltip-y: 782px; --md-tooltip-0: -16px;"><div class="md-tooltip" id="__code_2_annotation_3" role="tooltip"><div class="md-tooltip__inner md-typeset">We use <a class="autorefs autorefs-internal" href="../api/models/function/#pydantic_ai.models.function.FunctionModel"><code>FunctionModel</code></a> to replace the agent's model with our custom function.</div></div><a href="#__code_2_annotation_3" class="md-annotation__index" tabindex="-1"><span data-md-annotation-id="3"></span></a></aside></span>
        <span class="n">prompt</span> <span class="o">=</span> <span class="s1">'What will the weather be like in London on 2032-01-01?'</span>
        <span class="k">await</span> <span class="n">run_weather_forecast</span><span class="p">([(</span><span class="n">prompt</span><span class="p">,</span> <span class="n">user_id</span><span class="p">)],</span> <span class="n">conn</span><span class="p">)</span>

    <span class="n">forecast</span> <span class="o">=</span> <span class="k">await</span> <span class="n">conn</span><span class="o">.</span><span class="n">get_forecast</span><span class="p">(</span><span class="n">user_id</span><span class="p">)</span>
    <span class="k">assert</span> <span class="n">forecast</span> <span class="o">==</span> <span class="s1">'The forecast is: Rainy with a chance of sun'</span>
</code></pre></div>
<ol hidden="">
<li></li>
<li></li>
<li></li>
</ol>
<h3 id="overriding-model-via-pytest-fixtures">Overriding model via pytest fixtures</h3>
<p>If you're writing lots of tests that all require model to be overridden, you can use <a href="https://docs.pytest.org/en/6.2.x/fixture.html">pytest fixtures</a> to override the model with <a class="autorefs autorefs-internal" href="../api/models/test/#pydantic_ai.models.test.TestModel"><code>TestModel</code></a> or <a class="autorefs autorefs-internal" href="../api/models/function/#pydantic_ai.models.function.FunctionModel"><code>FunctionModel</code></a> in a reusable way.</p>
<p>Here's an example of a fixture that overrides the model with <code>TestModel</code>:</p>
<div class="language-python highlight"><span class="filename">tests.py</span><pre id="__code_3"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_3 > code"></button><code><span class="kn">import</span><span class="w"> </span><span class="nn">pytest</span>
<span class="kn">from</span><span class="w"> </span><span class="nn">weather_app</span><span class="w"> </span><span class="kn">import</span> <span class="n">weather_agent</span>

<span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_ai.models.test</span><span class="w"> </span><span class="kn">import</span> <span class="n">TestModel</span>


<span class="nd">@pytest</span><span class="o">.</span><span class="n">fixture</span>
<span class="k">def</span><span class="w"> </span><span class="nf">override_weather_agent</span><span class="p">():</span>
    <span class="k">with</span> <span class="n">weather_agent</span><span class="o">.</span><span class="n">override</span><span class="p">(</span><span class="n">model</span><span class="o">=</span><span class="n">TestModel</span><span class="p">()):</span>
        <span class="k">yield</span>


<span class="k">async</span> <span class="k">def</span><span class="w"> </span><span class="nf">test_forecast</span><span class="p">(</span><span class="n">override_weather_agent</span><span class="p">:</span> <span class="kc">None</span><span class="p">):</span>
    <span class="o">...</span>
    <span class="c1"># test code here</span>
</code></pre></div>







  
  






                
              </article>
            </div>
          
          
  <script>var tabs=__md_get("__tabs");if(Array.isArray(tabs))e:for(var set of document.querySelectorAll(".tabbed-set")){var labels=set.querySelector(".tabbed-labels");for(var tab of tabs)for(var label of labels.getElementsByTagName("label"))if(label.innerText.trim()===tab){var input=document.getElementById(label.htmlFor);input.checked=!0;continue e}}</script>

<script>var target=document.getElementById(location.hash.slice(1));target&&target.name&&(target.checked=target.name.startsWith("__tabbed_"))</script>
        </div>
        
      </main>
      
        <footer class="md-footer">
  
  <div class="md-footer-meta md-typeset">
    <div class="md-footer-meta__inner md-grid">
      <div class="md-copyright">
  
    <div class="md-copyright__highlight">
      © Pydantic Services Inc. 2024 to present
    </div>
  
  
</div>
      
    </div>
  </div>
</footer>
      
    </div>
    <div class="md-dialog" data-md-component="dialog">
      <div class="md-dialog__inner md-typeset"></div>
    </div>
    
    
    <script id="__config" type="application/json">{"base": "..", "features": ["search.suggest", "search.highlight", "content.tabs.link", "content.code.annotate", "content.code.copy", "content.code.select", "navigation.path", "navigation.indexes", "navigation.sections", "navigation.tracking", "toc.follow"], "search": "../assets/javascripts/workers/search.f8cc74c7.min.js", "translations": {"clipboard.copied": "Copied to clipboard", "clipboard.copy": "Copy to clipboard", "search.result.more.one": "1 more on this page", "search.result.more.other": "# more on this page", "search.result.none": "No matching documents", "search.result.one": "1 matching document", "search.result.other": "# matching documents", "search.result.placeholder": "Type to start searching", "search.result.term.missing": "Missing", "select.version": "Select version"}}</script>
    
    
      <script src="../assets/javascripts/bundle.f1b6f286.min.js"></script>
      
        <script src="/flarelytics/client.js"></script>
      
        <script src="https://cdn.jsdelivr.net/npm/algoliasearch@5.20.0/dist/lite/builds/browser.umd.js"></script>
      
        <script src="https://cdn.jsdelivr.net/npm/instantsearch.js@4.77.3/dist/instantsearch.production.min.js"></script>
      
        <script src="/javascripts/algolia-search.js"></script>
      
    
  <script id="init-glightbox">const lightbox = GLightbox({"touchNavigation": true, "loop": false, "zoomable": true, "draggable": true, "openEffect": "zoom", "closeEffect": "zoom", "slideEffect": "slide"});
document$.subscribe(() => { lightbox.reload() });
</script>
</body></html>