# Hakyll Migration Requirements
**Date**: June 16, 2025  
**Purpose**: Complete Jekyll to Hakyll migration for Animal Rationis Capax  
**Goal**: Full control, enhanced Chamber functionality, private hosting  

---

## 🎯 Migration Objectives

### **Primary Goals**
1. **Complete platform independence** - off GitHub, onto private server
2. **Enhanced Chamber functionality** - better AI integration, protected sessions
3. **Advanced typography** - Pandoc AST manipulation for superior rendering
4. **Authentication system** - protect internal materials properly
5. **Professional infrastructure** - ready for funding and scaling

### **IP Protection Requirements**
- **Maintain all legal timestamps** and priority documentation
- **Enhanced privacy** for raw session materials
- **Complete control** over access and permissions
- **No external dependencies** that could change terms

---

## 📋 Current System Inventory

### **Jekyll Architecture (Current)**
- **Version**: Jekyll 3.8.3
- **Theme**: Modified Klisé theme with extensive customizations
- **Hosting**: GitHub Pages (master branch auto-deploy)
- **Domain**: davidglidden.eu (custom domain)
- **Posts**: 74+ posts with sophisticated semantic typing
- **Collections**: 3 Chamber collections with complex cross-referencing

### **Content Structure**
```
Site Root/
├── _posts/ (74+ posts, many with photo essays)
├── _chamber_canon/ (8+ fictional works)
├── _chamber_deliberations/ (published sessions)
├── _chamber_meta/ (meta-commentary)
├── chamber/ (public pages)
├── docs/ (internal documentation)
├── assets/ (images, fonts, CSS)
└── _sass/ (custom SCSS modules)
```

### **Key Features to Preserve**
1. **Semantic post types** (13 types: observation, fragment, essay, etc.)
2. **Ornamental system** (breathing marks for each semantic type)
3. **Typography system** (EB Garamond, IBM Plex, custom utilities)
4. **Chamber functionality** (voice tracking, cross-references, canon)
5. **Navigation systems** (enfilade, semantic archives)
6. **Responsive design** (8px rhythm grid, mobile-first)

### **Custom SCSS Modules**
- `_typography.scss` - Custom font stack and utilities
- `_chamber.scss` - Chamber-specific styling
- `_utilities.scss` - Semantic type classes
- `_navigation.scss` - Enfilade and archive navigation
- `_post.scss` - Content styling
- `_mobile-responsive.scss` - Responsive design

---

## 🛠️ Technical Requirements

### **Server Infrastructure Needed**
- **VPS or dedicated server** with root access
- **Domain control** (davidglidden.eu transfer from GitHub Pages)
- **SSL certificate** management
- **Backup strategy** for complete site and data

### **Hakyll Capabilities Required**
1. **Collections support** - equivalent to Jekyll collections
2. **Custom metadata** - complex frontmatter handling
3. **Cross-referencing** - dynamic linking between content types
4. **SCSS compilation** - maintain existing stylesheet architecture
5. **Custom routing** - preserve current URL structure
6. **Pandoc integration** - enhanced typography and AST manipulation

### **Authentication System**
- **Public content** - open access (current Chamber pages)
- **Research tier** - academic access with agreements
- **Internal tier** - private documentation (docs/internal/)
- **Session tier** - raw Chamber materials (chamber-sessions-private/)

### **Enhanced Chamber Features**
1. **Session processing automation** - from raw files to published deliberations
2. **Bibliography engine** - automatic cross-referencing and authority tracking
3. **Voice pattern analysis** - enhanced tracking across sessions
4. **Search functionality** - within Chamber materials
5. **Export systems** - various formats for different users

---

## 📂 Content Migration Mapping

### **Direct Migrations**
- **Posts** → Hakyll posts (maintain semantic types)
- **Pages** → Hakyll pages (preserve navigation)
- **Assets** → Static files (fonts, images, CSS)
- **Collections** → Hakyll collections or custom content types

### **Enhanced Functionality**
- **Chamber sessions** → Protected processing pipeline
- **Bibliography** → Dynamic authority tracking
- **Voice patterns** → Advanced analytics
- **Cross-references** → Automated linking

### **New Capabilities**
- **Authentication** → Tiered access control
- **Advanced typography** → Pandoc AST manipulation
- **Session automation** → Raw file processing
- **Search** → Full-text indexing
- **Analytics** → Private usage tracking

---

## 🔐 Security & Privacy Requirements

### **Access Control Levels**
1. **Public** - Current Chamber pages, blog posts
2. **Research** - Select materials for academic consortium
3. **Internal** - Complete documentation and protocols
4. **Private** - Raw sessions and processing materials

### **Data Protection**
- **No external analytics** (Google, etc.)
- **Self-hosted fonts** (maintain current approach)
- **No CDN dependencies** (complete independence)
- **GDPR compliance** (EU-based, privacy-first)

### **Backup Strategy**
- **Full site backups** with git versioning
- **Database backups** if needed for authentication
- **Asset preservation** (images, documents)
- **Historical preservation** (all Jekyll history)

---

## 📊 Migration Timeline & Phases

### **Phase 1: Infrastructure Setup**
- [ ] Server provisioning and configuration
- [ ] Hakyll installation and basic configuration
- [ ] Domain transfer preparation
- [ ] SSL certificate setup

### **Phase 2: Content Migration**
- [ ] Jekyll content export and analysis
- [ ] Hakyll site structure creation
- [ ] SCSS/CSS system migration
- [ ] Typography system preservation

### **Phase 3: Chamber Enhancement**
- [ ] Collections migration (canon, deliberations, meta)
- [ ] Cross-referencing system recreation
- [ ] Voice tracking functionality
- [ ] Bibliography engine enhancement

### **Phase 4: Authentication & Privacy**
- [ ] User authentication system
- [ ] Tiered access control
- [ ] Private session handling
- [ ] Internal documentation protection

### **Phase 5: Testing & Launch**
- [ ] Complete functionality testing
- [ ] Content verification and linking
- [ ] Performance optimization
- [ ] Domain migration and DNS update

---

## 🧪 Testing Requirements

### **Functionality Tests**
- [ ] All internal links working
- [ ] Semantic type rendering correct
- [ ] Chamber cross-references functional
- [ ] Typography rendering properly
- [ ] Responsive design preserved

### **Performance Tests**
- [ ] Page load times acceptable
- [ ] Image optimization effective
- [ ] CSS/JS minification working
- [ ] Search functionality responsive

### **Security Tests**
- [ ] Authentication system secure
- [ ] Access control enforced
- [ ] Private content protected
- [ ] No information leakage

---

## 💾 Backup & Rollback Plan

### **Pre-Migration Backup**
- [ ] Complete Jekyll site archive
- [ ] GitHub repository clone
- [ ] All images and assets preserved
- [ ] Database of current functionality

### **Rollback Strategy**
- [ ] GitHub Pages can be restored quickly
- [ ] Domain can be reverted if needed
- [ ] All content preserved in multiple formats
- [ ] No data loss tolerance

---

## 📈 Success Criteria

### **Must-Have (Migration Success)**
- [ ] All existing content accessible
- [ ] All functionality preserved
- [ ] No broken links or missing content
- [ ] Typography and design identical
- [ ] Chamber features fully functional

### **Should-Have (Enhanced Success)**
- [ ] Authentication system working
- [ ] Enhanced Chamber features active
- [ ] Performance improvements visible
- [ ] Search functionality operational

### **Nice-to-Have (Optimal Success)**
- [ ] Advanced typography enhancements
- [ ] Automated session processing
- [ ] Enhanced bibliography engine
- [ ] Analytics and insights

---

## 🔍 Information Needed for Migration

### **Current Infrastructure**
- [ ] Complete Jekyll configuration review
- [ ] Custom code and modifications catalog
- [ ] Plugin usage and dependencies
- [ ] Image and asset inventory
- [ ] Current performance metrics

### **Target Infrastructure**
- [ ] Server specifications and access
- [ ] Domain management access
- [ ] SSL certificate approach
- [ ] Email and contact forms handling

### **Content Analysis**
- [ ] All collections and content types mapped
- [ ] Custom metadata usage documented
- [ ] Cross-reference patterns identified
- [ ] Image and asset requirements

### **Feature Requirements**
- [ ] Authentication system specifications
- [ ] Chamber enhancement priorities
- [ ] Typography improvement goals
- [ ] Search and discovery needs

---

## 📞 Support & Maintenance Plan

### **Ongoing Development**
- [ ] Feature enhancement pipeline
- [ ] Content management workflow
- [ ] Session processing automation
- [ ] System monitoring and maintenance

### **Documentation Requirements**
- [ ] Complete Hakyll configuration documentation
- [ ] Content management procedures
- [ ] Authentication and user management
- [ ] Troubleshooting and maintenance guides

---

**Migration Readiness**: Infrastructure and planning phase complete
**Next Step**: Server setup and Hakyll environment preparation
**Timeline**: Complete migration within 1-2 weeks
**Support**: Full migration assistance and post-migration optimization